from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('latvanyossagok',views.latvanyossagData),
    path('torles/<int:LatId>',views.deleteLatvanyossag, name="deleteLatvanyossag"),
    path('telepulesek',views.telepulesData),
    path('TelepulesTorles/<int:TelepId>',views.deleteTelepules, name="deleteTelepules"),
    path('orszagok',views.orszagData),
    path('OrszagTorles/<int:OrId>',views.deleteOrszag, name="deleteOrszag"),
]
