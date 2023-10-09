from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('details/', views.details_view, name='details'),
    path('<int:id>/', views.update_record, name='updatedata'),
]