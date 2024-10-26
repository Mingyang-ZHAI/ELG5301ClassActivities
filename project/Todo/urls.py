from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_todo, name="list-todo"),
    path('create/', views.create_todo, name="create-todo"),
    path('retrieve/<str:id>/', views.retrieve_todo, name="retrieve-todo"),
    path('update/<str:id>/', views.update_todo, name="update-todo"),
    path('delete/<str:id>/', views.delete_todo, name="delete-todo"),
]
