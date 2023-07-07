from rest_framework import serializers

from Locale.models import Region, State, LGA, City


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = "__all__"


class StateSerializer(serializers.ModelSerializer):
    region = serializers.CharField(source="region.name", read_only=True)
    lgas = serializers.StringRelatedField(many=True, read_only=True)
    cities = serializers.StringRelatedField(many=True, read_only=True)
    
    class Meta:
        model = State
        fields = "__all__"


class LGASerializer(serializers.ModelSerializer):
    class Meta:
        model = LGA
        fields = "__all__"


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"