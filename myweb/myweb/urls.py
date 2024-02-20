from django.contrib import admin
from django.urls import include, path

from django.views.generic import TemplateView

from polls.views import views_page

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
    path("link/", include("polls.urls")),
    path("page65/", views_page, name="page"),
]