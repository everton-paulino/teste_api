from django.urls import path
from app.views import cadastro_list, cadastro_detail_change_delete


urlpatterns = [
    path('', cadastro_list),
    path('<int:pk>/', cadastro_detail_change_delete)
    
]

