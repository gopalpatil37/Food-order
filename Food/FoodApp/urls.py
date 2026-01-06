from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_view,name="home"),
    path('about/',views.about_view,name="about"),
    path('menu/',views.menu_view,name="menu"),
    path('book/',views.about_view,name="book"),
    path('book-table/',views.book_view,name="book"),
]
