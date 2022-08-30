from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages

def index(request):
    return render(request, "index.html")

def register(request):
    if request.method == 'POST':
        errors = User.objects.validator(request.POST)
        if errors:
            for error in errors:
                messages.error(request, errors[error])
            return redirect('/')
        # create new user 
        new_user = User.objects.create(
            first_name = request.POST['f_n'],
            last_name = request.POST['l_n'],
            email = request.POST['email'],
            password = request.POST['password']
        )
        # store new user data in session
        request.session['user_id'] = new_user.id
        request.session['name'] = f"{new_user.first_name} {new_user.last_name}"
        return redirect('/home')


def login(request):
    if request.method == 'POST':
        # filters for a user using the inputted email
        logged_user = User.objects.filter(email=request.POST['email'])
        if logged_user:
            logged_user = logged_user[0] # reassigning to be value inside of list
            if logged_user.password == request.POST['password']:
                request.session['user_id'] = logged_user.id
                request.session['name'] = f"{logged_user.first_name} {logged_user.last_name}"
                return redirect('/home')
            else:
                messages.error(request, "Incorrect Password")
        else:
            messages.error(request, "Email does not exits")
    return redirect('/home')

def logout(request):
    request.session.clear()
    return redirect('/')

def render_home(request):
    context = {
        'all_posts': Post.objects.all()
    }
    return render(request, "home.html", context) 

def submit_post(request, post_id):
    if request.method == "POST":
        new_post = Post.objects.create(content=request.POST['content'], creator=User.objects.get(id=request.session['user_id']))
        print(new_post)
        return redirect('/home')