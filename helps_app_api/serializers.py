from rest_framework import serializers
from helps_app.models import HelpRequest, Region, City

class HelpRequestSerializer(serializers.ModelSerializer):
    """Готовый сериализатор"""
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = HelpRequest
        fields = "__all__"

class CitySerializer(serializers.ModelSerializer):
    """Готовый сериализатор"""
    class Meta:
        model = City
        fields = "__all__"

class RegionSerializer(serializers.ModelSerializer):
    """Готовый сериализатор"""
    class Meta:
        model = Region
        fields = "__all__"

# class HelpRequestWithSerializer(serializers.Serializer):
#     """Сериализатор модели HelpRequest написанный вручную"""
#     citi_name_id = serializers.IntegerField()
#     user_id = serializers.IntegerField()
#     title = serializers.CharField()
#     text = serializers.CharField()
#     pub_date = serializers.DateTimeField()
#     update = serializers.DateTimeField()
#     contacts = serializers.CharField()
#
# class RegionSerializer(serializers.Serializer):
#     """Сериализатор модели Regions"""
#     region_name = serializers.CharField()
#
#     def create(self, validated_data):
#         return Region.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.region_name = validated_data.get('region_name')
#         instance.save()
#         return instance
