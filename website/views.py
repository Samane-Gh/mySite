# an connector that connect url to user requests
from django.shortcuts import render
from django.http import HttpResponse 
from django.http import JsonResponse
def index_view(request):
    return  render (request ,'index.html')
def about_view(request):
    return  render (request ,'about.html')
def contact_view(request):
    return  render (request ,'contact.html')

# Create your views here.
