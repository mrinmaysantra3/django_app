from dataclasses import fields
from  rest_framework import serializers
from base.models import Player

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields='__all__'
