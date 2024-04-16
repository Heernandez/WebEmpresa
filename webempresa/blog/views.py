from django.shortcuts import render,get_object_or_404
from .models import Post, Category
# Create your views here.

def blog(request):
    blogs = Post.objects.all()
    return render(request,"blog/blog.html",{"blogs":blogs})


def category(request,category_id):
    category = get_object_or_404(Category,id=category_id)
    #blog = Post.objects.filter(categories=category)
    return render(request,"blog/category.html",{"category":category}) #, "blogs":blog})
