from . import views
from django.urls import path

app_name = 'food'

urlpatterns = [
    path('', views.IndexClassView.as_view(), name='index'),
    path('<int:pk>/', views.FoodDetail.as_view(), name='detail'),
    path('new/', views.create_item, name='create_item'),
    path('<int:pk>/edit/', views.edit, name='edit_item'),
    path('<int:pk>/delete/', views.delete, name='delete_item'),
]