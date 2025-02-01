from rest_framework import serializers 
from parcel.models import Parcel, Taker

# for Parcel serializer
class ParcelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcel
        fields = "__all__"

# for taker serializer
class TakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taker 
        fields = "__all__"