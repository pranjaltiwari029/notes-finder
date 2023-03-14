from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('ai/',views.ai,name="ai"),
    path('dm/',views.dm,name="dm"),
    path('ime/',views.ime,name="ime"),
    path('java/',views.java,name="java"),
    path('pd/',views.pd,name="pd"),
    path('se/',views.se,name="se"),
    path('ds/',views.ds,name="ds"),
    path('sd/',views.sd,name="sd"),
    path('ns/',views.ns,name="ns"),
    
]