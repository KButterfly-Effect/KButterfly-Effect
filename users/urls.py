from django.urls import path
from .views import *

app_name = "users"

urlpatterns = [
    path("mypage", mypage, name="mypage"),
    path("makelist",makelist,name="makelist"),
    path("deletelist",deletelist,name="deletelist"),
    path("updatelist/<int:id>",updatelist,name="updatelist"),
    path("addlist/<int:post_id>",addlist,name="addlist"),
    path("todolist/",todolist,name="todolist"),
]