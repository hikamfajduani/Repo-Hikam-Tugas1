from django.shortcuts import render
from katalog.models import CatalogItem

def index(request):
    return render(request, 'index.html')
