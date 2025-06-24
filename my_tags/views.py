from django.shortcuts import render
import datetime
import markdown
from django.utils.safestring import mark_safe
from .models import Blog

# Create your views here.
def index(request): 
    return render(request, 'index.html', {"message": "welcome to django"})

def about(request): 
    return render(request, 'about.html')

def contact(request): 
    return render(request, 'contact.html')

def signup(request): 
    return render(request, 'signup.html')

def login(request): 
    return render(request, 'login.html')

def filter_demo(request): 
    context = {
        "my_string": "HELLO world",
        "my_date": datetime.date(2025,6,18),
        "long_string": "This is a long sring to be displayed",
        "my_len": ["We are learning django", "python"],
        "empty_var":None ,
        "skills":["python", "java", "kotlin"],
        "string2": "python programming",
        "string3": "Hello\nwelcome to\npython programming",
    }
    return render(request, 'filters.html', context)

def blog_list(request):
    blogs = Blog.objects.prefetch_related('editors').all()
    for blog in blogs:
        blog.rendered_text = mark_safe(markdown.markdown(blog.text))
    return render(request, 'blog_list.html', {'blogs': blogs})