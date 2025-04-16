from django.urls import path
from acc import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('smtp/', views.smtp, name='smtp'),
]