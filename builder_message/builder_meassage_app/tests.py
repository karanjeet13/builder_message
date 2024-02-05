import unittest
from inspect import isclass, ismethod
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
            self.message_builder = Message()

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
            return self.message_builder

class TestMessageBuilder(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.outer_class = Message
        cls.inner_class = MessageBuilder.Builder
        cls.original_class = Message

    def test_builder_class_has_static_class(self):
        self.assertTrue(isclass(self.inner_class), "If the builder pattern is implemented, the builder class should be an inner class")
        self.assertTrue(self.inner_class.__name__.startswith("_"), "If the builder pattern is implemented, the builder class should be static")

    def test_builder_class_has_all_fields(self):
        original_fields = set(self.original_class.__dict__.keys())
        builder_fields = set(self.inner_class().__dict__.keys())
        self.assertTrue(original_fields.issubset(builder_fields), "If the builder pattern is implemented, the builder class should have a field for each field in the original class")

    def test_inner_fields(self):
        inner_class_fields = set(self.inner_class().__dict__.keys())
        has_reference = hasattr(self.inner_class, 'message_builder')
        self.assertTrue(has_reference or inner_class_fields.issuperset(self.original_class.__dict__.keys()), "If the builder pattern is implemented, the builder class should have either a reference to the original class or all its fields")

    def test_builder_class_has_build_method(self):
        builder_methods = [method for method in dir(self.inner_class) if ismethod(getattr(self.inner_class, method))]
        build_method = next((method for method in builder_methods if method == "build"), None)
        self.assertIsNotNone(build_method, "If the builder pattern is implemented, the builder class should have a build method")

    def test_build_method_copies_values(self):
        self.assertTrue(hasattr(self.inner_class, 'build'), "If the builder pattern is implemented, the builder class should have a build method")

if __name__ == "__main__":
    unittest.main()
