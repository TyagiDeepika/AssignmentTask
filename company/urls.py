from django.contrib import admin
from django.urls import path, include
from api_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('companyapp.urls')),
    path('api/', include('api_app.urls')),

]
