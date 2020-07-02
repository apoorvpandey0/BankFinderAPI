from django.urls import path

from . import views

urlpatterns=[
    path('',views.BankListAPIView.as_view(),name = 'api-bank-list'),
]
