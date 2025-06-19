from django.contrib import admin
from django.urls import path, include
from application import views



urlpatterns = [
    path('', views.ent_reg),
    path('registration/', views.registration, name="reg"),
    path('entrance/', views.entrance, name="ent"),
    path('main', views.main),
    path('registration/postuser/', views.postuser),
    path('admin/', admin.site.urls)
]
