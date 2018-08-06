from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = "main"

urlpatterns = [
    path("", views.index, name="index"),
    path("About", views.about, name="about"),
    path("Tools", views.tools, name="tools"),
    path("Learning", views.learning, name="learning"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)