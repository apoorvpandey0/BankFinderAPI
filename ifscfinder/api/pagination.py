from rest_framework.pagination import PageNumberPagination

class BankPageNumberPagination(PageNumberPagination):
    page_size = 50
