from rest_framework import serializers
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

from nft_token.models import Token
from nft_token.api.services import mint_token
from bntm.utils import create_hash



class CreateTokenSerializer(serializers.Serializer):
    owner = serializers.CharField(max_length=50)
    media_url = serializers.CharField(max_length=200, required=False)
    tx_hash = serializers.CharField(required=False)
    unique_hash = serializers.CharField(required=False)

    def validate_media_url(self, value):
        try:
            URLValidator()(value)
        except ValidationError:
            raise serializers.ValidationError("failed to validate media url")
        return value

    def create(self, validated_data):
        validated_data["unique_hash"] = create_hash()
        validated_data["tx_hash"] = mint_token(
            validated_data["owner"], validated_data["media_url"], validated_data["unique_hash"]
        )
        return Token.objects.create(**validated_data)
