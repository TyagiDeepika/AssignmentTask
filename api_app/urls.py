
from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.ApiOverview, name='home'),
    path('list/', views.show_list, name='list'),
    path('list/<str:pk>/', views.show_user, name='list'),
    path('add_user/', views.add_user, name='add_user'),
    path('update_user/<str:pk>/', views.update_user, name='update_user'),
    path('delete_user/<str:pk>/', views.delete_user, name='delete_user')
]


