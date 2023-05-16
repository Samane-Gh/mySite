from django.shortcuts import render,get_object_or_404
from blog.models import Post
from django.utils import timezone
# Create your views here.
def blog_view(request,pid=1):
    #posts = Post.objects.filter(status=1).order_by('title')
    posts = Post.objects.order_by('published_date')
    contex = {'posts': posts}
    return render(request,'blog/blog-home.html',contex)

def blog_single(request,pid=None):
    if pid is None:
        contex = {'post': {}}
        return render(request,'blog/blog-single.html',contex)        
    post = Post.objects.get(id =pid)
    post.counted_views +=1
    post.save()

    next_post = Post.objects.filter(published_date__gt=post.published_date).order_by('published_date').first()
    prev_post =Post.objects.filter(published_date__lt=post.published_date).order_by('published_date').last()
    contex = {'post': post,'next_post': next_post,'prev_post': prev_post}
    
    post.save()
    return render(request,'blog/blog-single.html',contex)
    

def test(request):
    
    return render(request,'test.html')



    

