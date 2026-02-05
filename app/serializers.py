from rest_framework import serializers 
from .models import Player_Serializer


class PlayerSerializer(serializers.Serializer):
    name=serializers.CharField()
    age=serializers.IntegerField()
    country=serializers.CharField()
    jersy_number=serializers.IntegerField()
    def create(self, validated_data):
        return Player_Serializer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.age = validated_data.get("age", instance.age)
        instance.country = validated_data.get("country", instance.country)
        instance.jersy_number = validated_data.get("jersy_number", instance.jersy_number)
        instance.save()
        return instance