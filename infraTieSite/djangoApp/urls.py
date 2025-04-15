'''
* Filename: models.py
* Author: InfraTie
* Edited by: Justin Moua
* 
* NOTES: A file of URL paths. 
* All the views used are imported from "from . import views" which is from
* views.py which is in the same directory as this urls.py file.
*       
*
'''
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