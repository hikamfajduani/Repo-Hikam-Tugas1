from django.urls import path
from todolist.views import show_todolist, register, login_user, logout_user, create, selesai,hapus,show_todolist_json,create_json

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create/', create, name='create'),
    path('change_status/<int:id>', selesai, name='change_status'),
    path('delete/<int:id>', hapus, name='delete'),
    path("json/", show_todolist_json, name="show_todolist_json"),
    path("add/", create_json, name="create_json"),
]