from django.shortcuts import render, redirect
from todolist.models import IsiTodolist
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect, HttpRequest
from django.urls import reverse
from todolist.form import CreateTodoForm

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    user = request.user
    data_todolist = IsiTodolist.objects.all().filter(user=request.user)
    context = {
    'list_todo': data_todolist,
    'nama' : user.username,
    'last_login': request.COOKIES['last_login'],
    }
    return render(request, "todolist.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # login(request, user)
            # return redirect('todolist:show_todolist')
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request: HttpRequest):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/todolist/login/')
def create(request):
    form = CreateTodoForm(request.POST)
    if request.method == 'POST':
        form = CreateTodoForm(request.POST, request.FILES)
        if form.is_valid():
            task = IsiTodolist(
                todo_date=str(datetime.datetime.now().date()),
                todo_title=form.cleaned_data["title"],
                todo_description=form.cleaned_data["description"],
                user=request.user,
            )
            task.save()
            return redirect('todolist:show_todolist')
    else:
        form = CreateTodoForm(initial={'user': request.user})
    context = {"form": form}
    return render(request, 'create.html', context)
 
@login_required(login_url='/todolist/login/')
def selesai(request, id):
    task = IsiTodolist.objects.get(pk = id)
    task.is_finished = not task.is_finished
    task.save()
    return redirect('todolist:show_todolist')

@login_required(login_url='/todolist/login/')
def hapus(request, id):
    task = IsiTodolist.objects.get(pk = id)
    task.delete()
    return redirect('todolist:show_todolist')
