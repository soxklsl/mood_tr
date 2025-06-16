from django.contrib import admin
from django.urls import path
from application import views

urlpatterns = [
    path('', views.main),
    path('ent_reg', views.ent_reg),
    path('registration/', views.registration),
    path('admin/', admin.site.urls)
]
