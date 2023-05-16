from django.shortcuts import render,get_object_or_404
from blog.models import Post
from blog.models import Category
from django.utils import timezone
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.
def blog_view(request,**kwargs):
    #posts = Post.objects.filter(status=1).order_by('title')
    posts = Post.objects.filter(status=1).order_by('published_date')
    if kwargs.get('cat_name') != None:
        posts = posts.filter(Category__name=kwargs['cat_name'])
    if kwargs.get('ather_name') != None:
        posts = posts.filter(auther__username =kwargs['ather_name'])   
    posts = Paginator(posts,3) 
    try: 
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
    contex = {'posts': posts}
    return render(request,'blog/blog-home.html',contex)


def blog_single(request,pid=None):
    if pid is None:
        contex = {'post': {}}
        return render(request,'blog/blog-single.html',contex)        
    post = Post.objects.get(id =pid)
    post.counted_views +=1
    next_post = Post.objects.filter(published_date__gt=post.published_date).order_by('published_date').first()
    prev_post =Post.objects.filter(published_date__lt=post.published_date).order_by('published_date').last()
    contex = {'post': post,'next_post': next_post,'prev_post': prev_post}
    post.save()
    return render(request,'blog/blog-single.html',contex)
    
def blog_category(request,cat_name):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(Category__name=cat_name)
    contex ={'posts': posts}
    return render(request,'blog/blog-home.html',contex)

def test(request):   
    return render(request,'test.html')

def blog_search(request):
    posts = Post.objects.filter(status=1)
    if request.method == 'GET' :
        if request.GET.get('s'):
           posts = posts.filter(content__contains=request.GET.get('s')) 
        #print(request.GET.get('s'))
        
    contex = {'posts': posts}
    return render(request,'blog/blog-home.html',contex)    



    

