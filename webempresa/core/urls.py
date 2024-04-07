
from django.urls import path
from . import views 
urlpatterns = [
    path("", views.home, name="homePage"),
    path("about/", views.about, name="aboutPage"),
    path("services/", views.services, name="servicesPage"),
    path("store/", views.store, name="storePage"),
    path("contact/", views.contact, name="contactPage"),
    path("blog/", views.blog, name="blogPage"),
    path("sample/", views.blog, name="samplePage"),
]
