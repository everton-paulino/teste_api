from django.urls import path
from app.views import CadastroListAndCreate, Cadastro_detail_change_delete

urlpatterns = [
    path('', CadastroListAndCreate.as_view()),
    path('<int:pk>/', Cadastro_detail_change_delete.as_view()),
]