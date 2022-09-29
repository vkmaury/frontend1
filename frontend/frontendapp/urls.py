from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('save', views.save, name='save'),
    path('update/<str:id>', views.update, name='update'),
    path('edit', views.edit, name='edit'),
    path('delete/<str:id>', views.delete, name='delete'),



]
