from django.urls import path
from Studentapp import views

urlpatterns=[
    path("",views.registration),
    path('success/',views.success,name='success')
]