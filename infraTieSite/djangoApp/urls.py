from django.urls import path
from . import views
urlpatterns=[
    #path("", views.login, name="login"), #Login page created.
    path("", views.HomePageView, name='HomePageView'),
    path("loginView/", views.loginView, name='loginView'),
    path("inspection/", views.inspection_view, name="inspection"), #Inspection page created.
    path("base/", views.baseView, name="base"), #debugging purposes.
]