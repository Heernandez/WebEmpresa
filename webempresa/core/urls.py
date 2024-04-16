from django.urls import path
from . import views 
urlpatterns = [
    path("", views.home, name="homePage"),
    path("about/", views.about, name="aboutPage"),
    path("store/", views.store, name="storePage"),
    #path("contact/", views.contact, name="contactPage"),
]
