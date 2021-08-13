from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def perfumes(request):
    return render(request, 'perfumes/index.html')