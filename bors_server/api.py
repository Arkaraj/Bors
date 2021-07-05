from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer, DogSerializer
from .models import User, Dog


# Create your views here.


class UserViewSet(APIView):
    def get(self, request):
        users = User.objects.all().order_by("id")
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        pass


@api_view(['GET'])
def getAllDogs(request):
    dogs = Dog.objects.all().order_by("id")
    serializer = DogSerializer(dogs, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getSpecificDog(request, id=None):
    # pk - primary key
    dog = Dog.objects.get(id=id)
    serializer = DogSerializer(dog)
    return Response(serializer.data)


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
