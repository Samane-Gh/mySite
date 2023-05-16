from django import template
from blog.models import Post
register = template.Library()

@register.simple_tag(name='totalposts')

def function():
    posts = Post.objects.filter(status=1)
    return posts

@register.inclusion_tag('popularposts.html')
def popularposts():
    posts = Post.objects.filter(status=1).order_by('published_date')[:3]
    return {'posts': posts}
