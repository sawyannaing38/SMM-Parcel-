from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework import status 
from parcel.models import Parcel, Taker 
from .serializer import ParcelSerializer, TakerSerializer

# Create your views here.
@api_view(["PATCH"])
def take(request, id):
    
    # Try to get the parcel of id = id 
    try:
        parcel = Parcel.objects.get(pk=id)
    # handle does not exist error
    except Parcel.DoesNotExist:
        return Response({"message" : "Does Not Exist"}, status=status.HTTP_404_NOT_FOUND)

    # create serializer
    parcelSerializer = ParcelSerializer(parcel, data=request.data, partial=True)
    
    if parcelSerializer.is_valid():
        parcelSerializer.save()
        return Response(parcelSerializer.data, status=status.HTTP_200_OK)
    
    # if not valie
    return Response(parcelSerializer.errors, status=status.HTTP_400_BAD_REQUEST)


# For Creating Taker
@api_view(["POST"])
def create(request):

    # creating new serializer
    takerSerializer = TakerSerializer(data=request.data)

    if takerSerializer.is_valid():
        takerSerializer.save()
        return Response(takerSerializer.data, status=status.HTTP_201_CREATED)
    
    # if invalid
    return Response(takerSerializer.errors, status=status.HTTP_400_BAD_REQUEST)