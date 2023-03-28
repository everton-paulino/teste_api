from django.db import models

# Create your models here.

class Cadastro(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    created_at = models.DateField(auto_now_add=True) 
