from django.shortcuts import render
from .models import Project

# Create your views here.
def portfolio(request):
    projects=Project.objects.all()  # obtener todos los objetos generados desde el modelo / lista de registros en la BDD
    return render(request, "portfolio/portfolio.html", {'projects':projects})