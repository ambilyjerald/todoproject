from django.urls import path

from my_app import views

urlpatterns = [
    path("",views.todo,name="test"),
    path("dashboard",views.dash,name="test1"),
    path("dashadmin",views.dashadmin,name='test2')
]
