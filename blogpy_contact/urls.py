from django.urls import path
from .views import about_us,contact_us

urlpatterns = [
    path("about_us", about_us, name="about_us"),
    path("contact_us", contact_us, name="contact_us"),
]
