from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer, DogSerializer
from .models import User, Dog


@api_view(['GET'])
def getAllDogs(request):
    dogs = Dog.objects.all().order_by("id")
    serializer = DogSerializer(dogs, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getSpecificDog(request, id=None):
    dog = Dog.objects.get(id=id)
    serializer = DogSerializer(dog)
    return Response(serializer.data)


@api_view(['POST'])
def addDog(request):
    serializer = DogSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def addOwnerToDog(request, id):
    dog = Dog.objects.get(id=id)
    serializer = DogSerializer(instance=dog, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def removeDog(request, id=None):
    dog = Dog.objects.get(id=id)
    dog.delete()
    return Response("Deleted item sucessfully!")


@api_view(['GET'])
def getAllUsers(request):
    users = User.objects.all().order_by("id")
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getSpecificUser(request, id=None):
    # pk - primary key
    user = User.objects.get(id=id)
    serializer = UserSerializer(user)
    return Response(serializer.data)


@api_view(['POST'])
def addUser(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
