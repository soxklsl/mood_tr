from django.contrib import admin
from django.urls import path
from application import views

urlpatterns = [
    path('main', views.main),
    path('', views.ent_reg),
    path('registration/', views.registration),
    path('entrance/', views.entrance),
    path('admin/', admin.site.urls)
]
