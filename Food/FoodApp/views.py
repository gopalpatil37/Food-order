from django.shortcuts import render

# Create your views here.

def home_view(request):
    return render(request,'FoodApp/index.html')

def about_view(request):
    return render(request,'FoodApp/about.html')

def menu_view(request):
    return render(request,'FoodApp/menu.html')

def book_view(request):
    return render(request,'FoodApp/book.html')