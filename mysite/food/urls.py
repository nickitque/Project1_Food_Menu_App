from . import views
from django.urls import path

app_name = 'food'

urlpatterns = [
    path('', views.index, name='index'),
    path('item/', views.item, name='item'),
    path('<int:pk>/', views.detail, name='detail'),
    path('new/', views.create_item, name='create_item'),
    path('<int:pk>/edit/', views.edit, name='edit_item')
]