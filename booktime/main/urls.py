
from django.contrib import admin
from django.urls import path, include

from main import views
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path(
        "about-us/",
        TemplateView.as_view(template_name="about_us.html"),
        name = 'about_us',
        ),
    path(
        "",
        TemplateView.as_view(template_name="home.html"),
        name = 'home',
        ),

    path(
        "contact-us/",
        views.ContactUsView.as_view(),
        name="contact_us",
    ),
]
