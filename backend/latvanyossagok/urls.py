from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('latvanyossagok',views.latvanyossagData),
    path('torles/<int:LatId>',views.deleteLatvanyossag, name="deleteLatvanyossag"),
]
