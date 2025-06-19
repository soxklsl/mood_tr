from django.contrib import admin
from django.urls import path
from application import views

urlpatterns = [
    path('main', views.main),
    path('', views.ent_reg),
    path('registration/', views.registration, name="reg"),
    path('entrance/', views.entrance, name="ent"),
    path('admin/', admin.site.urls)
]
