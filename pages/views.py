from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')
    
def listings(request):
    return render(request, 'pages/listings.html')

def listing(request):
    return render(request, 'pages/listing.html')

def blogs(request):
    return render(request, 'pages/blogs.html')

def blog(request):
    return render(request, 'pages/blog.html')

def contact(request):
    return render(request, 'pages/contact.html')

def elements(request):
    return render(request, 'pages/elements.html')
