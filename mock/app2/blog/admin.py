from django.contrib import admin

# Register your models here.
# here the db looks and regsiters our model 
import site 

from .models import BlogPost

#some other crap for admin realted stuff
class BlogPostAdmin(admin.ModelAdmin):
    list_display=('title','timestamp')

admin.site.register(BlogPost,BlogPostAdmin)
