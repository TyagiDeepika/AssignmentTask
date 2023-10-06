from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import serializers
from companyapp.models import User,Company
from .serializer import UserSerializer,CompanySerializer
from rest_framework.response import Response



@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'List_User': '/list/',
        'List_User': '/list/pk',
        'show_user':"/show_user/",
        'Update': '/update_user/pk',
        'Delete': '/delete_user/pk/delete'
    }

    return Response(api_urls)

@api_view(['GET'])
def show_list(request):
    try:
        user_obj = User.objects.all()
        serializer = UserSerializer(user_obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

@api_view(['GET'])
def show_user(request,pk):
    try:
        user_obj = User.objects.get(id=pk)
        serializer = UserSerializer(user_obj, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

@api_view(['POST'])
def add_user(request):
    try:
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("user Delete Succsesfully !!!")
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

@api_view(['POST'])
def update_user(request,pk):
    try:
        user_obj = User.objects.get(id=pk)
        serializer = UserSerializer(instance =user_obj, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    


@api_view(['DELETE'])
def delete_user(request,pk):
    try:
        user_obj = User.objects.get(id=pk)
        user_obj.delete()
        
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    