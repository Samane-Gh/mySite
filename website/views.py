# an connector that connect url to user requests
from django.shortcuts import render
from django.http import HttpResponse 
from django.http import JsonResponse
def index_view(request):
    return  HttpResponse('<h1>This is Home page</h1>')
def about_view(request):
    return  HttpResponse('<h1>This is About page</h1>')
def contact_view(request):
    return  HttpResponse('<h1>This is Contact page</h1>')

# Create your views here.
