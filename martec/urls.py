from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # Portuguese naming for index url path.
    path("produtos/", views.products, name="products"),
    path("sobre_nos/", views.about_us, name="about_us"),
    path("contato/", views.contact, name="contact"),
]
