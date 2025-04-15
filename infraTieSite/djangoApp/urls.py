from django.urls import path
from . import views
urlpatterns=[
    path("", views.HomePageView, name='HomePageView'),
    path("loginView/", views.loginView, name='loginView'),
    path("inspection/", views.inspectionView, name="inspection"),
    #path("base/", views.baseView, name="base"), #debugging purposes.
    path("inspection/condition/<int:foreignKeyId>", views.conditionView, name="conditionView"),
    path("logout/", views.logoutView, name = "logout"),
]