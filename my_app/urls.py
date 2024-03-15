from django.urls import path

from my_app import views

urlpatterns = [
    path("",views.todo,name="test"),
    path("dashboard",views.dash,name="test1"),
    path("dashadmin",views.dashadmin,name='test2'),
    path('forms',views.formhtml,name='test3'),
    path('new',views.new,name='test4'),
    path('child',views.data,name='test5')
]
