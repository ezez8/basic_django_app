from channels.generic.websocket import AsyncJsonWebsocketConsumer
import json


class NotificationConsumer(AsyncJsonWebsocketConsumer):

	async def connect(self):
		"""
		Called when the websocket is handshaking as part of initial connection.
		"""
		print("NotificationConsumer: connect: " + str(self.scope["user"]) )
		await self.accept()


	async def disconnect(self, code):
		"""
		Called when the WebSocket closes for any reason.
		"""
		print("NotificationConsumer: disconnect")


	async def receive_json(self, content):
		"""
		Called when we get a text frame. Channels will JSON-decode the payload
		for us and pass it as the first argument.
		"""
		command = content.get("command", None)
		await self.send(json.dumps({'message': command}))