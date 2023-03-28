from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from app.models import Cadastro
from app.serializers import CadastroSerializer
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound


@api_view(['GET', 'POST'])
def cadastro_list(request):
    if request.method=='GET':
        cadastro = Cadastro.objects.all()
        serializer = CadastroSerializer(cadastro, many=True)
        return Response(serializer.data)



# @api_view(['GET', 'POST'])
# def cadastro_list(request):
#     if request.method=='GET':
#         cadastro = Cadastro.objects.all()
#         serializer = CadastroSerializer(cadastro, many=True)
#         return Response(serializer.data)
    
#     elif request.method=='POST':
#         try:
#             data = request.data
#             name = data['name']
#             cpf = data.get('cpf','000.000.000/00')
#             cadastro = Cadastro(name=name , cpf=cpf)
#             save_return = cadastro.save()
#             print('save all people',save_return)
#             return Response(data)
#         except Exception as e:
#             response = Response()
#             response.status_code = 500
#             response_content_dict = {'message': 'Internal Server Error - Everton'}             
#             response.content = response_content_dict
#             return response
#     else:
#         response = Response()
#         response.status_code = 500
#         response.content = 'Internal Server Error'
#         return response
