# an connector that connect url to user requests
from django.shortcuts import render
from django.http import HttpResponse 
from django.http import JsonResponse
from website.models import Contact
from website.forms import NameForm,ContactForm
def index_view(request):
    return  render (request ,'website/index.html')
def about_view(request):
    return  render (request ,'website/about.html')
def contact_view(request):
    return  render (request ,'website/contact.html')

def test(request):   
    if request.method == 'POST' :
        form = ContactForm(request.POST)
        if form.is_valid():
           form.save()
           return HttpResponse('Done')
        else:
            return HttpResponse('Not valid')
    form = ContactForm()
    return render(request,'test.html',{'form': form})
# Create your views here.
