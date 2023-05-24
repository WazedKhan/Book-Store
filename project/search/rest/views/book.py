from django.db.models import Count, Q

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView

from ..serializers import book
from book.models import Book


class SearchBooksList(ListAPIView):
    """search's book with related fields"""

    queryset = Book.objects.all()
    serializer_class = book.SearchBooksSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["name"]

    def get_queryset(self):
        keyword = self.request.query_params.get("keyword", None)
        queryset = super().get_queryset()
        if keyword:
            queryset = queryset.filter(
                Q(author__name__icontains=keyword.lower())
                | Q(name__icontains=keyword.lower())
                | Q(publisher__name__icontains=keyword.lower())
            ).order_by("author__name")

        return queryset
