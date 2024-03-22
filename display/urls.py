
from django.urls import path
from display import views


urlpatterns = [
    path('', views.get_template_dashboard, name='decision-machine'),
]
