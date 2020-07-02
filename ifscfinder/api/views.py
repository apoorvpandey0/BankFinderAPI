from rest_framework.generics import ListAPIView,RetrieveAPIView
from rest_framework.permissions import (AllowAny,IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly,)
from rest_framework.filters import (SearchFilter,OrderingFilter)
from rest_framework.pagination import (LimitOffsetPagination,PageNumberPagination)

from django.db.models import Q
from django_filters import rest_framework as filters

from ..models import Bank
from .pagination import BankPageNumberPagination
from .serializers import BankListSerializer,BankDetailSerializer

class BankDetailAPIView(RetrieveAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankDetailSerializer

class BankListAPIView(ListAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankListSerializer
    pagination_class = BankPageNumberPagination

    filter_backends =(filters.DjangoFilterBackend,SearchFilter,OrderingFilter)
    filterset_fields = ("bank_name",'bank_id','district','state','branch','ifsc','city','address')
    search_fields = ["bank_name",'bank_id','district','state','branch','ifsc','city','address']
