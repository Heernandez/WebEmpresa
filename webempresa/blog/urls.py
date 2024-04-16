
from django.urls import path
from . import views 
urlpatterns = [
    path("", views.blog, name="blogPage"),
    path("category/<int:category_id>/", views.category, name="categoryPage"),
]
