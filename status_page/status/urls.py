from django.urls import path
from .views import status_page
from . import views

urlpatterns = [
    path("", status_page, name="status_page"),
    path('report/', views.uptime_report, name='uptime_report'),
]
