from django.urls import path
from . import views
urlpatterns=[
    path ('',views.home),
    path ('sellpage/',views.sellpage),
    path ("base/",views.basepage),
    path ('user/',views.userpage),
]