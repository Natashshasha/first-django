from django.http import HttpResponse
from django.shortcuts import render

def main_page(request):
    return render(request, "index.html")

def about_page(request):
    return render(request, "about.html")

def post_page(request):
    return render(request, "post.html")
