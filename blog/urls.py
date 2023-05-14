
from django.urls import path
from blog.views import *

app_name ='blog'

urlpatterns = [
    
    #path("url addres ", "view")
    path('',blog_view,name='index' ),
    path('single/<int:pid>',blog_single,name='single'),
    path('single',blog_single,name='single'),
    path('post-<int:pid>',test,name='test'),
   
    
    
] 