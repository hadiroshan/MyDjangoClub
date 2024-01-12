from django.urls import path
from . import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns=[
    path("members/",views.ShowInfo,name="members"),
]
urlpatterns+=staticfiles_urlpatterns()

