# from djangochannelsrestframework.decorators import action
# from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
# from djangochannelsrestframework.observer.generics import ObserverModelInstanceMixin
# from channels.db import database_sync_to_async
# from channels.layers import get_channel_layer
# from .models import Card
# from QrCodesManagement.models import QRCode  
# from userManagement.models import CustomUser
# from .serializers import *
# from datetime import datetime
# import qrcode
# from django.conf import settings
# from django.core.mail import send_mail
# import io
# from django.core.files.base import ContentFile
# import random as rn

# class CardConsumer(ObserverModelInstanceMixin, GenericAsyncAPIConsumer):
#     queryset = Card.objects.all()
#     serializer_class = CardSerializer
#     lookup_field = "pk"

#     async def connect(self):
#         self.group_name = "card_updates"
#         await self.channel_layer.group_add(self.group_name, self.channel_name)
#         await super().connect()

#     async def disconnect(self, close_code):
#         await self.channel_layer.group_discard(self.group_name, self.channel_name)
#         await super().disconnect(close_code)

#     @action()
#     async def create_card(self, card_data, **kwargs):
#         try:
#             card = await self._create_card(card_data)
#             # Generate QR code for the card
#             qr_code = await self._generate_qr_code(card)
#             emails = await self.send_confirmation_email(card.owner.email, card.owner.name, card)

#             channel_layer = get_channel_layer()
#             await channel_layer.group_send(
#                 self.group_name,
#                 {
#                     'type': 'card_created',
#                     'card': CardSerializer(card).data
#                 }
#             )
#             await self.send_json({
#                 "action": "card_created",
#                 "card": CardSerializer(card).data,
#                 "qr_code": qr_code.code_value,  # Include QR code value in the response
#                 "qr_code_image": qr_code.image.url,  # Include the QR code image URL
#                 "emails": emails.subject  # Include a list of all the emails sent to the owner
#             })
#         except Exception as e:
#             await self.send_json({
#                 "action": "error",
#                 "message": str(e)
#             })

#     @action()
#     async def read_card(self, card_id, **kwargs):
#         try:
#             card = await self._read_card(card_id)
#             await self.send_json({
#                 "action": "read_card",
#                 "card": CardSerializer(card).data
#             })
#         except Exception as e:
#             await self.send_json({
#                 "action": "error",
#                 "message": str(e)
#             })

#     @action()
#     async def update_card(self, card_data, **kwargs):
#         try:
#             card = await self._update_card(card_data)
#             channel_layer = get_channel_layer()
#             await channel_layer.group_send(
#                 self.group_name,
#                 {
#                     'type': 'card_updated',
#                     'card': CardSerializer(card).data
#                 }
#             )
#             await self.send_json({
#                 "action": "card_updated",
#                 "card": CardSerializer(card).data
#             })
#         except Exception as e:
#             await self.send_json({
#                 "action": "error",
#                 "message": str(e)
#             })

#     @action()
#     async def delete_card(self, card_id, **kwargs):
#         try:
#             await self._delete_card(card_id)
#             channel_layer = get_channel_layer()
#             await channel_layer.group_send(
#                 self.group_name,
#                 {
#                     'type': 'card_deleted',
#                     'card_id': card_id
#                 }
#             )
#             await self.send_json({
#                 "action": "card_deleted",
#                 "card_id": card_id
#             })
#         except Exception as e:
#             await self.send_json({
#                 "action": "error",
#                 "message": str(e)
#             })

#     async def card_created(self, event):
#         await self.send_json({
#             "action": "card_created",
#             "card": event['card']
#         })

#     async def card_updated(self, event):
#         await self.send_json({
#             "action": "card_updated",
#             "card": event['card']
#         })

#     async def card_deleted(self, event):
#         await self.send_json({
#             "action": "card_deleted",
#             "card_id": event['card_id']
#         })

#     @database_sync_to_async
#     def _create_card(self, card_data):
#         issued_date_str = card_data.get('issued_date')
#         expiry_date_str = card_data.get('expiry_date')
#         personal = CustomUser.objects.get(pk=card_data['owner'])
#         issued_date = datetime.strptime(issued_date_str, '%Y-%m-%d').date() if issued_date_str else None
#         expiry_date = datetime.strptime(expiry_date_str, '%Y-%m-%d').date() if expiry_date_str else None
#         cardnum = rn.randint(0, 100000000000000000)

#         return Card.objects.create(
#             card_number=cardnum,
#             card_type=card_data['card_type'],
#             owner=personal,
#             issued_date=issued_date,
#             expiry_date=expiry_date,
#             is_active=card_data['is_active'],
#             daily_scan_count=card_data['count'],
#             last_scan_date=card_data['scans']
#         )

#     @database_sync_to_async
#     def _read_card(self, card_id):
#         return Card.objects.get(pk=card_id)

#     @database_sync_to_async
#     def _update_card(self, card_data):
#         card = Card.objects.get(pk=card_data['id'])
#         card.card_number = card_data.get('card_number', card.card_number)
#         card.card_type = card_data.get('card_type', card.card_type)
#         card.is_active = card_data.get('is_active', card.is_active)
#         card.daily_scan_count = card_data.get('count', card.daily_scan_count)
#         card.last_scan_date = card_data.get('scans', card.last_scan_date)
#         card.save()
#         return card

#     @database_sync_to_async
#     def _delete_card(self, card_id):
#         card = Card.objects.get(pk=card_id)
#         card.delete()

#     @database_sync_to_async
#     def _generate_qr_code(self, card):
#         # Generate a unique code for the QR
#         code_value = rn.randint(0, 100000000000000000)  # Generate a random number for QR code
#         # Create QR code image
#         qr_img = qrcode.make(f'Qr Identification : {code_value} , \n \n Card : {card.card_number} , \n \n User_profile: {card.owner.profile} \n \n  Card_Owner: {card.owner.name}')
#         # Save the QR code to a bytes buffer
#         buffer = io.BytesIO()
#         qr_img.save(buffer, format='PNG')
#         buffer.seek(0)  # Reset buffer position to the beginning
#         qr_code_file = ContentFile(buffer.getvalue(), name=f"qr_code_{code_value}:card :_{card.card_number}.png")

#         # Create and save QRCode instance with the image and data
#         qr_code_instance = QRCode.objects.create(
#             code_value=code_value,
#             associated_card=card,
#             owner=card.owner,  # Associate the QR code with the owner of the card
#             image=qr_code_file  # Save the generated image to the image field
#         )
        
#         # Send the confirmation email after creating the QR code
    
#         return qr_code_instance  # Return the QR code instance provided
    
#     @database_sync_to_async
#     def send_confirmation_email(self, email, name, qr_code):
#         subject = "MasterCard Tech Ltd - Card Creation Confirmation"
#         message = (
#             f"Hello {name},\n\n"
#             f"Your card has been created successfully.\n\n"
#             f"The QR code value for your card is {qr_code.code_value}.\n\n"
#             "Please keep this information safe.\n\n"
#             "Best Regards,\n"
#             "MasterCard Tech Ltd"
#         )
#         from_email = settings.EMAIL_HOST_USER
#         recipient_list = [email]

#         try:
#             send_mail(subject, message, from_email, recipient_list)
#             print(f"Email sent successfully to {email}")  # Debug statement
#         except Exception as e:
#             print(f"Failed to send email: {e}")


from djangochannelsrestframework.decorators import action
from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.observer.generics import ObserverModelInstanceMixin
from channels.db import database_sync_to_async
from channels.layers import get_channel_layer
from .models import Card
from QrCodesManagement.models import QRCode  
from userManagement.models import CustomUser
from .serializers import CardSerializer  # Ensure you have imported your serializer
from datetime import datetime
import qrcode
from django.conf import settings
from django.core.mail import send_mail
import io
from django.core.files.base import ContentFile
import random as rn

class CardConsumer(ObserverModelInstanceMixin, GenericAsyncAPIConsumer):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    lookup_field = "pk"

    async def connect(self):
        self.group_name = "card_updates"
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await super().connect()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)
        await super().disconnect(close_code)

    @action()
    async def create_card(self, card_data, **kwargs):
        try:
            card = await self._create_card(card_data)  # Create the Card instance
            qr_code = await self._generate_qr_code(card)  # Generate the QR code

            # Send confirmation email after creating the QR code
            await self.send_confirmation_email(card.owner.email, card.owner.name, qr_code)

            channel_layer = get_channel_layer()
            await channel_layer.group_send(
                self.group_name,
                {
                    'type': 'card_created',
                    'card': CardSerializer(card).data,
                }
            )
            
            # Send JSON response with QR code details
            await self.send_json({
                "action": "card_created",
                "card": CardSerializer(card).data,
                "qr_code": qr_code.code_value,  # Access QR code value
                "qr_code_image": qr_code.image.url,  # Access QR code image URL
            })
        except CustomUser.DoesNotExist:
            await self.send_json({
                "action": "error",
                "message": "The specified owner does not exist."
            })
        except Exception as e:
            await self.send_json({
                "action": "error",
                "message": str(e)
            })

    @action()
    async def read_card(self, card_id, **kwargs):
        try:
            card = await self._read_card(card_id)
            await self.send_json({
                "action": "read_card",
                "card": CardSerializer(card).data
            })
        except Exception as e:
            await self.send_json({
                "action": "error",
                "message": str(e)
            })

    @action()
    async def update_card(self, card_data, **kwargs):
        try:
            card = await self._update_card(card_data)
            channel_layer = get_channel_layer()
            await channel_layer.group_send(
                self.group_name,
                {
                    'type': 'card_updated',
                    'card': CardSerializer(card).data
                }
            )
            await self.send_json({
                "action": "card_updated",
                "card": CardSerializer(card).data
            })
        except Exception as e:
            await self.send_json({
                "action": "error",
                "message": str(e)
            })

    @action()
    async def delete_card(self, card_id, **kwargs):
        try:
            await self._delete_card(card_id)
            channel_layer = get_channel_layer()
            await channel_layer.group_send(
                self.group_name,
                {
                    'type': 'card_deleted',
                    'card_id': card_id
                }
            )
            await self.send_json({
                "action": "card_deleted",
                "card_id": card_id
            })
        except Exception as e:
            await self.send_json({
                "action": "error",
                "message": str(e)
            })

    async def card_created(self, event):
        await self.send_json({
            "action": "card_created",
            "card": event['card']
        })

    async def card_updated(self, event):
        await self.send_json({
            "action": "card_updated",
            "card": event['card']
        })

    async def card_deleted(self, event):
        await self.send_json({
            "action": "card_deleted",
            "card_id": event['card_id']
        })

    @database_sync_to_async
    def _create_card(self, card_data):
        issued_date_str = card_data.get('issued_date')
        expiry_date_str = card_data.get('expiry_date')
        personal = CustomUser.objects.get(pk=card_data['owner'])
        issued_date = datetime.strptime(issued_date_str, '%Y-%m-%d').date() if issued_date_str else None
        expiry_date = datetime.strptime(expiry_date_str, '%Y-%m-%d').date() if expiry_date_str else None
        cardnum = rn.randint(0, 100000000000000000)

        return Card.objects.create(
            card_number=cardnum,
            card_type=card_data['card_type'],
            owner=personal,
            issued_date=issued_date,
            expiry_date=expiry_date,
            is_active=card_data['is_active'],
            daily_scan_count=card_data['count'],
            last_scan_date=card_data['scans']
        )

    @database_sync_to_async
    def _read_card(self, card_id):
        return Card.objects.get(pk=card_id)

    @database_sync_to_async
    def _update_card(self, card_data):
        card = Card.objects.get(pk=card_data['id'])
        card.card_number = card_data.get('card_number', card.card_number)
        card.card_type = card_data.get('card_type', card.card_type)
        card.is_active = card_data.get('is_active', card.is_active)
        card.daily_scan_count = card_data.get('count', card.daily_scan_count)
        card.last_scan_date = card_data.get('scans', card.last_scan_date)
        card.save()
        return card

    @database_sync_to_async
    def _delete_card(self, card_id):
        card = Card.objects.get(pk=card_id)
        card.delete()

    @database_sync_to_async
    def _generate_qr_code(self, card):
        # Generate a unique code for the QR
        code_value = rn.randint(0, 100000000000000000)  # Generate a random number for QR code
        # Create QR code image
        qr_img = qrcode.make(f'Qr Identification : {code_value}, \n\n Card : {card.card_number}, \n\n User_profile: {card.owner.profile}, \n\n Card_Owner: {card.owner.name}')
        # Save the QR code to a bytes buffer
        buffer = io.BytesIO()
        qr_img.save(buffer, format='PNG')
        buffer.seek(0)  # Reset buffer position to the beginning
        qr_code_file = ContentFile(buffer.getvalue(), name=f"qr_code_{code_value}:card :_{card.card_number}.png")

        # Create and save QRCode instance with the image and data
        qr_code_instance = QRCode.objects.create(
            code_value=code_value,
            associated_card=card,
            owner=card.owner,  # Associate the QR code with the owner of the card
            image=qr_code_file  # Save the generated image to the image field
        )
        
        return qr_code_instance  # Return the QR code instance provided
    
    @database_sync_to_async
    def send_confirmation_email(self, email, name, qr_code):
        subject = "MasterCard Tech Ltd - Card Creation Confirmation"
        message = (
            f"Hello {name},\n\n"
            f"Your card has been created successfully.\n\n"
            f"The QR code value for your card is {qr_code.code_value}.\n\n"
            "Please keep this information safe.\n\n"
            "Best Regards,\n"
            "MasterCard Tech Ltd"
        )
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email]

        print(f"Preparing to send email to {email}")  # Debug statement
        try:
            send_mail(subject, message, from_email, recipient_list)
            print(f"Email sent successfully to {email}")  # Debug statement
        except Exception as e:
            print(f"Failed to send email: {e}")  # Log the exception