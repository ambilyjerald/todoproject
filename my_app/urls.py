from django.urls import path

from my_app import views

urlpatterns = [
    path("",views.todo,name="test"),
    path("dashboard",views.dash,name="test1"),
    # path("dash1",views.dash1,name='test2')
]
