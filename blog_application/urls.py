"""
URL configuration for blog_application project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from blogs import views

admin.site.site_header = "Blogs Admin"
admin.site.index_title = "Blogs Information"

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path("blogs/",views.blogs, name="blogs"),
    path("join/",views.join, name="join"),
    path("save", views.join_save, name="join_save"),
    path("login/",views.login, name="login"),
    path("create/",views.login_save, name="login_save"),
    path("dashboard/",views.dashboard, name="dashboard"),
    path("add", views.add_blogs, name="add_blogs"),
    path("blog_details/<int:blo_id>", views.blog_details, name="blog_details"),
    path("all_blogs/",views.all_blogs,name="all_blogs"),
]
