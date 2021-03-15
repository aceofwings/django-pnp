from channels.generic.websocket import WebsocketConsumer

class PNPConsumer(WebsocketConsumer):

    def connect(self):
        self.accept()

    def receive(self, text_data=None, bytes_data=None):
        pass
    def disconnect(self, close_code):
        pass
