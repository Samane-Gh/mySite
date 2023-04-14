from django.http import HttpResponse 
from django.http import JsonResponse
def http_test(request):
    return  HttpResponse('<h1>This is a Test</h1>')
def jason_test(request):
    return JsonResponse({"name" : 'Samane'})