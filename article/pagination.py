from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
# class GlobalPagination(PageNumberPagination):
#     page_size = 15
#     page_size_query_param = 'page_size'
#     max_page_size = 50


class CustomPagination(PageNumberPagination):
    page_size = 8
    page_query_param = "page_no"
    max_page_size = 20
    page_size_query_param = "page_size"

    def get_paginated_response(self,data):
        return Response({
    'page_info': {
        'current_page': self.page.number,
        'total_pages': self.page.paginator.num_pages,
        'next': self.get_next_link(),
        'previous': self.get_previous_link(),
    },
    'items_info': {
        'total_items': self.page.paginator.count,
        'page_size': self.get_page_size(self.request),
    },
    'results': data,
    })

    