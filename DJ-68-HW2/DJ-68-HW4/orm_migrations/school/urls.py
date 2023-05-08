from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from school.views import StudentList

urlpatterns = [
    path('', StudentList.as_view(), name='students'),
]
