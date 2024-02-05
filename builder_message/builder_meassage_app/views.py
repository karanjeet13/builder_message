from enum import Enum

class MessageType(Enum):
    TEXT = "TEXT"
    IMAGE = "IMAGE"
    AUDIO = "AUDIO"
    VIDEO = "VIDEO"

class Message:
    def __init__(self, message_type, content, sender, recipient, is_delivered, timestamp):
        self.message_type = message_type
        self.content = content
        self.sender = sender
        self.recipient = recipient
        self.is_delivered = is_delivered
        self.timestamp = timestamp

class MessageBuilder:
    @staticmethod
    def builder():
        return MessageBuilder.Builder()

    class Builder:
        def __init__(self):
            self.message_builder = MessageBuilder()

        def message_type(self, message_type):
            self.message_builder.message_type = message_type
            return self

        def content(self, content):
            self.message_builder.content = content
            return self

        def sender(self, sender):
            self.message_builder.sender = sender
            return self

        def recipient(self, recipient):
            self.message_builder.recipient = recipient
            return self

        def is_delivered(self, is_delivered):
            self.message_builder.is_delivered = is_delivered
            return self

        def timestamp(self, timestamp):
            self.message_builder.timestamp = timestamp
            return self

        def build(self):
            message_builder = MessageBuilder()
            message_builder.message_type = self.message_builder.message_type
            message_builder.content = self.message_builder.content
            message_builder.sender = self.message_builder.sender
            message_builder.recipient = self.message_builder.recipient
            message_builder.is_delivered = self.message_builder.is_delivered
            message_builder.timestamp = self.message_builder.timestamp
            return message_builder

