from django.urls import path

from .views import ListPetView, CreatePetView, export_pets

urlpatterns = (
    path('', ListPetView.as_view(), name='list_pets'),
    path('export/', export_pets, name='export_pets'),
    path('create/', CreatePetView.as_view(), name='create_pet'),
)
