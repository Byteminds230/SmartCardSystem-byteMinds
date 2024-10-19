
# from djangochannelsrestframework.decorators import action
# from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
# from djangochannelsrestframework.observer.generics import ObserverModelInstanceMixin
# from channels.db import database_sync_to_async
# from channels.layers import get_channel_layer
# from .models import Card
# from userManagement.models import CustomUser
# from .serializers import CardSerializer
# from datetime import datetime
# import json

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
#         print(f"Received card data: {card_data}")
#         try:
#             # Validate and create the card asynchronously
#             card = await self._create_card(card_data)
#             # Broadcast the created card to all clients
#             channel_layer = get_channel_layer()
#             await channel_layer.group_send(
#                 self.group_name,
#                 {
#                     'type': 'card_created',
#                     'card': CardSerializer(card).data
#                 }
#             )
#             # Send confirmation to the client who created the card
#             await self.send_json({
#                 "action": "card_created",
#                 "card": CardSerializer(card).data
#             })
#         except Exception as e:
#             # Send an error response if something goes wrong
#             await self.send_json({
#                 "action": "error",
#                 "message": str(e)
#             })

#     async def card_created(self, event):
#         # Send the created card details to the WebSocket
#         await self.send_json({
#             "action": "card_created",
#             "card": event['card']
#         })

#     @database_sync_to_async
#     def _create_card(self, card_data):
#         # Parse dates from strings to date objects
#         issued_date_str = card_data.get('issued_date')
#         expiry_date_str = card_data.get('expiry_date')
#         try:
#             personal = CustomUser.objects.get(pk=card_data['owner'])
#         except CustomUser.DoesNotExist:
#             raise ValueError("Owner not found")

#         issued_date = datetime.strptime(issued_date_str, '%Y-%m-%d').date() if issued_date_str else None
#         expiry_date = datetime.strptime(expiry_date_str, '%Y-%m-%d').date() if expiry_date_str else None

#         # Create the card instance
#         return Card.objects.create(
#             card_number=card_data['card_number'],
#             card_type=card_data['card_type'],
#             owner=personal,
#             issued_date=issued_date,
#             expiry_date=expiry_date,
#             is_active=card_data['is_active'],
#             daily_scan_count=card_data['count'],  # Default to 0 if count is not provided
#             last_scan_date=card_data['scans']  # Default to None if scans is not provided
#         )

from djangochannelsrestframework.decorators import action
from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.observer.generics import ObserverModelInstanceMixin
from channels.db import database_sync_to_async
from channels.layers import get_channel_layer
from .models import Card
from userManagement.models import CustomUser
from .serializers import CardSerializer
from datetime import datetime

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
            card = await self._create_card(card_data)
            channel_layer = get_channel_layer()
            await channel_layer.group_send(
                self.group_name,
                {
                    'type': 'card_created',
                    'card': CardSerializer(card).data
                }
            )
            await self.send_json({
                "action": "card_created",
                "card": CardSerializer(card).data
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

        return Card.objects.create(
            card_number=card_data['card_number'],
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