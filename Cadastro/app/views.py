from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from app.models import Cadastro
from app.serializers import CadastroSerializer
from django.shortcuts import render


@api_view(['GET', 'POST'])
def cadastro_list(request):
    if request.method=='GET':
        cadastro = Cadastro.objects.all()
        serializer = CadastroSerializer(cadastro, many=True)
        return Response(serializer.data)    
    elif request.method=='POST':
        serializer = CadastroSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def cadastro_detail_change_delete(request, pk):
    try:
        cadastro = Cadastro.objects.get(pk=pk)
    except Cadastro.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)   

    if request.method =='GET':
        serializer = CadastroSerializer(cadastro)
        return Response(serializer.data)
    elif request.method =='PUT':
        serializer = CadastroSerializer(cadastro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        cadastro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def index(request):
    return render(request, 'index.html')   

