from django.urls import path
from . import views

urlpatterns = [
    path('', views.group_list, name='group_list'),
    path('add/', views.add_group, name='add_group'),
    path('edit/<int:group_id>/', views.edit_group, name='edit_group'),
    path('delete/<int:group_id>/', views.delete_group, name='delete_group')
]