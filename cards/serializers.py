from rest_framework import serializers
from cards.models import Card

class CardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['id', 'texto']