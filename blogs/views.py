from django.shortcuts import render ,redirect
from django.http import HttpResponse
from .models import Registration, Blogs
from django.contrib import messages

def home(request):
    return render(request, "index.html")

def blogs(request):
    if request.method == "POST":
        blog_title = request.POST.get('search')
        blog = Blogs.objects.filter(title__icontains=blog_title)
    else:
        
        blog = Blogs.objects.all()[:5]

    return render(request, "blogs.html",{
        "blog":blog
    })


def join(request):
    return render(request, "join.html")


def join_save(request):
    if request.method == "POST":
        newUserName = request.POST.get('yourname')
        loginUsername = request.POST.get('username')

        if Registration.objects.filter(username=loginUsername).exists():
            messages.success(request, 'Username Already Exists.')
            return redirect('/join/')

        else:
            
            loginPassword = request.POST.get('password')

            join = Registration(yourname=newUserName,username=loginUsername, password=loginPassword)
            join.save()

            messages.success(request, "You are successfully join....")
            return redirect('/login/')
    return HttpResponse('404 - Not found ')


def login(request):
    return render(request, "login.html")

def login_save(request):
    if request.method == "POST":
        loginUsername = request.POST.get('username')
        loginPassword = request.POST.get('password')

        login = Registration.objects.filter(username=loginUsername, password=loginPassword).first()
        if login is not  None:
            username = login.username
            password = login.password
            messages.success(request, 'Your Successfully Login In.... ')
            return redirect('/dashboard/')
        else:
            messages.error(request, 'Your Email and password not exits...')
            return redirect('/login/')
        
        
    return HttpResponse('404 - Not Found')

def dashboard(request):
    return render(request, "dashboard.html")

def add_blogs(request):
    if request.method == "POST":
        title_blog = request.POST.get('title')
        description_blog = request.POST.get('description')

        dashboard = Blogs(title= title_blog, description = description_blog)
        dashboard.save()

        messages.success(request, "Your Blog Successfully Added.....")
        return redirect("/blogs/")
    
def blog_details(request, blo_id):
    blog = Blogs.objects.get(pk=blo_id)
    return render(request, "blog_details.html", {"blog": blog})

def all_blogs(request):
    if request.method == "POST":
        blog_title = request.POST.get('search')
        blog = Blogs.objects.filter(title__icontains=blog_title)
    else:
        blog = Blogs.objects.all()

    return render(request, "all_blogs.html",{
        "blog":blog
    })
