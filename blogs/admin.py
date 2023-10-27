from django.contrib import admin

from blogs.models import Registration
from blogs.models import Join
from blogs.models import Blogs

class RegistrationInfo(admin.ModelAdmin):
    list_display =('yourname', 'username', 'password')
    search_fields = ('username', )

class JoinInfo(admin.ModelAdmin):
    list_display = ('username', 'password')

class BlogsInfo(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title', )

admin.site.register(Registration, RegistrationInfo)
admin.site.register(Join, JoinInfo)
admin.site.register(Blogs, BlogsInfo)
