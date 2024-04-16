from django.urls import path
from . import views 
urlpatterns = [
    path("<slug:page_title>/", views.page, name="samplePage"),
]
