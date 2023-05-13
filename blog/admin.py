from django.contrib import admin
from blog.models import Post,Category

class PostAdmin(admin.ModelAdmin):
    #date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display =('title','auther', 'counted_views', 'status','published_date', )
    list_filter = ('status','auther', )
    search_fields = ['title','content']

admin.site.register(Category)
admin.site.register(Post,PostAdmin)


# Register your models here.
