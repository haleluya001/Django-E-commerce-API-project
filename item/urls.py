from django.urls import path
from . import views

app_name = 'item'


urlpatterns = [
    path('',views.items, name='items'),
    path('item/new/', views.new, name='new'),
    path('item/<int:pk>/', views.detail, name='item_detail'),
    path('item/<int:pk>/delete/', views.delete, name='item_delete'),
    path('item/<int:pk>/edit/', views.edit, name='edit'),
]