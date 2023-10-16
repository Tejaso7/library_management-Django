from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('home/', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('register/', views.Register.as_view(), name="register"),
    path('store/', views.store, name="store"),
    path('addBooks/', views.addBooks, name="addBooks"),
    path('deletebook/<int:pk>', views.deletebook, name="deletebook"),
    path('updateView/<int:pk>', views.updateView, name="updateView"),
    path('update/<int:pk>', views.update, name="update"),
    path('search/', views.search, name="search"),

#Jason responce API for local server Url="http://127.0.0.1:8000/booksjason/"
#Jason responce API in hosting platform url="http://domainname/booksjason/"

    path('booksjason/', views.book_list, name="book_list"),

]
