from rest_framework import serializers
from realEstate.models import *

class OfficeAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfficeAddress
        fields = '__all__'

class HouseAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseAddress
        fields = '__all__'

class OpeningHoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpeningHours
        fields = '__all__'

class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = '__all__'

class ImageOfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageOffice
        fields = '__all__'

class AgentSerializer(serializers.ModelSerializer):
    fullName = serializers.ReadOnlyField()
    class Meta:
        model = Agent
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = '__all__'

class ImageHouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageHouse
        fields = '__all__'