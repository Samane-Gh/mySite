from django.shortcuts import render,get_object_or_404
from blog.models import Post
from django.utils import timezone
# Create your views here.
def blog_view(request):
    #posts = Post.objects.filter(status=1)
    
    posts = Post.objects.filter(published_date__lte=timezone.now())
    contex = {'posts': posts}
    return render(request,'blog/blog-home.html',contex)

def blog_single(request,pid):

    post = get_object_or_404(Post,pk= pid)
    contex = {'post': post}
    return render(request,'blog/blog-single.html',contex)
    

def test(request,pid):
    #post = Post.objects.get(id=pid)
    post = get_object_or_404(Post,pk= pid)
    contex = {'post': post}
    return render(request,'test.html',contex)

def blog_post(request,pid):
    post = Post.objects.get(id=pid)
    contex ={'post' : post}
    post.counted_views = 10
    post.save()
    
    return render(request ,'blog/blog-home.html',contex)
    

