from rest_framework import request
from rest_framework.decorators import api_view
from .serializers import PassengerSerializer
from .models import Passenger
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def employeeView(request):
    if request.method == 'GET':
        passenger = Passenger.objects.all()
        serializer = PassengerSerializer( passenger, many = True)
        if serializer:
            print( "here" )
            return Response( data = serializer.data, status = status.HTTP_200_OK )
        else:
            return Response( data = serializer.errors, status = status.HTTP_400_BAD_REQUEST )
    
    
    if request.method == 'POST':
        serializer = PassengerSerializer(data = request.data)
        print( "data ", request.data )
        if serializer.is_valid():
            serializer.save()
            return Response("success", status = status.HTTP_200_OK )
        else:
            return Response( data = serializer.errors, status = status.HTTP_400_BAD_REQUEST )


@api_view(['GET', 'PUT', 'DELETE'])
def employeeViewById(request, name):
    try:
        passenger = Passenger.objects.get( pk = name )
    except:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PassengerSerializer( passenger )
        return Response( data = serializer.data, status = status.HTTP_200_OK )
       
    if request.method == 'PUT':
        serializer = PassengerSerializer(passenger , data = request.data)
        print( "data ", request.data )
        if serializer.is_valid():
            serializer.save()
            return Response("success", status = status.HTTP_200_OK )
        else:
            return Response( data = serializer.errors, status = status.HTTP_400_BAD_REQUEST )

    if request.method == 'DELETE':
        passenger.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


