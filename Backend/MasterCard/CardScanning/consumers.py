# from djangochannelsrestframework.decorators import action
# from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
# from djangochannelsrestframework.observer.generics import ObserverModelInstanceMixin
# from channels.db import database_sync_to_async
# from channels.layers import get_channel_layer
# from .models import Card
# from userManagement.models import CustomUser
# from .serializers import CardSerializer
# from datetime import datetime

# class CardConsumer(ObserverModelInstanceMixin, GenericAsyncAPIConsumer):
#     queryset = Card.objects.all()
#     serializer_class = CardSerializer
#     lookup_field = "pk"

#     async def connect(self):
#         self.group_name = "card_updates"
#         await self.channel_layer.group_add(self.group_name, self.channel_name)
#         await super().connect()

#     async def disconnect(self , close_code):
#         await self.channel_layer.group_discard(self.group_name, self.channel_name)
#         await super().disconnect(close_code)

#     @action()
#     async def create_card(self, card_data, **kwargs):
#         print(f"recieved card data: {card_data}")
#         try:
#             # Create the card asynchronously
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
#         personal = CustomUser.objects.get(pk = card_data['owner'])
#         issued_date = datetime.strptime(issued_date_str, '%Y-%m-%d').date() if issued_date_str else None
#         expiry_date = datetime.strptime(expiry_date_str, '%Y-%m-%d').date() if expiry_date_str else None

#         # Create the card instance
#         return Card.objects.create(
#             card_number =card_data['card_number'],
#             card_type = card_data['card_type'],
#             owner = personal,
#             issued_date = issued_date,
#             expiry_date = expiry_date,
#             is_active = card_data['is_active'],
#             daily_scan_count = card_data['count'],  
#             last_scan_date =card_data['scans']
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
import json

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
        print(f"Received card data: {card_data}")
        try:
            # Validate and create the card asynchronously
            card = await self._create_card(card_data)
            # Broadcast the created card to all clients
            channel_layer = get_channel_layer()
            await channel_layer.group_send(
                self.group_name,
                {
                    'type': 'card_created',
                    'card': CardSerializer(card).data
                }
            )
            # Send confirmation to the client who created the card
            await self.send_json({
                "action": "card_created",
                "card": CardSerializer(card).data
            })
        except Exception as e:
            # Send an error response if something goes wrong
            await self.send_json({
                "action": "error",
                "message": str(e)
            })

    async def card_created(self, event):
        # Send the created card details to the WebSocket
        await self.send_json({
            "action": "card_created",
            "card": event['card']
        })

    @database_sync_to_async
    def _create_card(self, card_data):
        # Parse dates from strings to date objects
        issued_date_str = card_data.get('issued_date')
        expiry_date_str = card_data.get('expiry_date')
        try:
            personal = CustomUser.objects.get(pk=card_data['owner'])
        except CustomUser.DoesNotExist:
            raise ValueError("Owner not found")

        issued_date = datetime.strptime(issued_date_str, '%Y-%m-%d').date() if issued_date_str else None
        expiry_date = datetime.strptime(expiry_date_str, '%Y-%m-%d').date() if expiry_date_str else None

        # Create the card instance
        return Card.objects.create(
            card_number=card_data['card_number'],
            card_type=card_data['card_type'],
            owner=personal,
            issued_date=issued_date,
            expiry_date=expiry_date,
            is_active=card_data['is_active'],
            daily_scan_count=card_data['count'],  # Default to 0 if count is not provided
            last_scan_date=card_data['scans']  # Default to None if scans is not provided
        )

    # async def receive_json(self, content, **kwargs):
    #     try:
    #         # Validate JSON content structure here if needed
    #         action = content.get("action")
    #         if action == "create_card":
    #             await self.create_card(content.get("data"))
    #         else:
    #             await self.send_json({"action": "error", "message": "Invalid action"})
    #     except json.JSONDecodeError as e:
    #         # Handle JSON decoding error gracefully
    #         await self.send_json({"action": "error", "message": f"Invalid JSON data: {str(e)}"})
    #     except Exception as e:
    #         # Handle other exceptions
    #         await self.send_json({"action": "error", "message": str(e)})
