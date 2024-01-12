from django.shortcuts import render , redirect , get_object_or_404
from .forms import RegisterForm , ContactForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import Blog , Project , Contact
from django.http import JsonResponse
import json
# Create your views here.
def home(request):
    return render(request,'home/index.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'home/login.html', {'success': "Registration successful. Please login."})
        else:
            error_message = form.errors.as_text()
            return render(request, 'register.html', {'error': error_message})

    return render(request,'home/register.html')


def login_view(request):
    if request.method=="POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return render(request,'home/index.html')
        else:
            return render(request, 'home/login.html', {'error': "Invalid credentials. Please try again."})

    return render(request,'home/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect("/login_view")


def allblog(request):
    allPosts =  Blog.objects.all()
    context = {'allPosts': allPosts}
    return render(request,'blogs/allblog.html',context)

def blogdetails(request,post_slug):
    post = get_object_or_404(Blog , slug=post_slug)
    context = {'post': post}
    return render(request,'blogs/blogdetails.html',context)


def allproject(request):
    allPosts =  Project.objects.all()
    context = {'allPosts': allPosts}
    return render(request,'projects/allprojects.html',context)

def projectdemo(request,post_slug):
    post = get_object_or_404(Project , slug=post_slug)
    context = {'post': post}
    return render(request,'projects/projectdemo.html',context)


def aboutme(request):
    return render(request,'home/aboutme.html')

def contactme(request):
    if request.method == 'POST':
        forms = ContactForm(request.POST , request.FILES)
        
        if forms.is_valid():
            forms.save()
        
        return redirect('home')
  
    return render(request,'home/contactus.html')
