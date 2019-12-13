from django.shortcuts import render
from .models import Portfolio

# Create your views here.

def project_index(request):
    portfolios = Portfolio.objects.all()
    return render(request,'portfolio/project_index.html',{'portfolios':portfolios})

def project_details(request,pk):
    portfolio = Portfolio.objects.get(pk=pk)
    return render(request,'portfolio/project_details.html',{'portfolio':portfolio})


