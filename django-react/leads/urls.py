from django.urls import path
from . import views
from .views import LeadListCreate

urlpatterns = [
    path('api/leads/', views.LeadListCreate.as_view()),
]