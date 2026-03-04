from rest_framework import serializers

class ContactRequestSerializer(serializers.Serializer):
    """Serializer for contact form request body"""
    name = serializers.CharField(max_length=128, required=True, help_text="Contact person's name")
    email = serializers.EmailField(required=True, help_text="Contact person's email address")
    phone = serializers.CharField(max_length=128, required=False, allow_blank=True, help_text="Contact person's phone number")
    message_subject = serializers.CharField(max_length=128, required=True, help_text="Subject of the message")
    message_body = serializers.CharField(required=True, help_text="Body of the message")
    add_to_mailer = serializers.BooleanField(required=False, default=False, help_text="Whether to add contact to mailing list")

class ContactResponseSerializer(serializers.Serializer):
    """Serializer for successful contact form submission"""
    name = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()
    message_subject = serializers.CharField()
    message_body = serializers.CharField()
    add_to_mailer = serializers.BooleanField()
    band_id = serializers.IntegerField()
