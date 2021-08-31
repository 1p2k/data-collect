import csv
from datetime import datetime
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, TemplateView

from .forms import PetForm
from .models import Pet


def export_pets(request):
    pets = Pet.objects.all()
    file = f'export_pets_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'

    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': f'attachment; filename="{file}"'},
    )

    writer = csv.writer(response)
    writer.writerow(('Name', 'Gender', 'Age', 'Food', 'Notes'))

    for pet in pets:
        writer.writerow((pet.name, pet.gender, pet.age, pet.food, pet.notes))

    return response


class IndexView(TemplateView):
    template_name = 'common/index.html'


class ListPetView(ListView):
    model = Pet
    template_name = 'pets/pet_list.html'
    context_object_name = 'pets'


class CreatePetView(CreateView):
    model = Pet
    form_class = PetForm
    success_url = reverse_lazy('list_pets')
    template_name = 'pets/pet_create.html'
