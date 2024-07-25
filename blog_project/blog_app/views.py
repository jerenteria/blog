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
        'all_posts': Post.objects.all(),
        'all_replies': Response.objects.all().order_by('-created_at')
    }
    return render(request, "home.html", context)


def submit_post(request):
    if request.method == "POST":
        new_post = Post.objects.create(
        content=request.POST['content'],
        creator=User.objects.get(id=request.session['user_id'])
        )
        print(new_post)
    return redirect('/home')

def reply(request, post_id):
    if request.method == "POST":
        # post_id is automatically created with django when a new object is created and saved to database(bc it inherits from models.Model which by defauly creates an auto-incrementing integer key field called 'id if you dont specify one')
        post = Post.objects.get(id=post_id) # retreving the post that you want to reply to(by getting the post_id)
        new_reply = Response.objects.create(
            text = request.POST['text'],
            responder=User.objects.get(id=request.session['user_id']),
            # first post is the field name in object Response if i would've named it "related_post" I wouldve put related_post = post instead
            post = post # first post refers to the field name in Response model, second post refers to the Post object you just retrieved(basically saying this response belong to this post)
        )
    return redirect('/home')