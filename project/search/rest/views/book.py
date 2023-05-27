from django.db.models import Case, IntegerField, Value, When, Q

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView

from ..serializers import book
from book.models import Stock


class SearchBooksList(ListAPIView):
    """search's book with related fields"""

    queryset = Stock.objects.all()
    serializer_class = book.SearchStockSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["id"]

    def get_queryset(self):
        keyword = self.request.query_params.get("keyword", None)
        queryset = super().get_queryset()
        if keyword:
            queryset = (
                queryset.filter(
                    Q(book__author__name__icontains=keyword.lower())
                    | Q(book__name__icontains=keyword.lower())
                    | Q(book__publisher__name__icontains=keyword.lower())
                ).annotate(
                    relevance=Case(
                        When(book__name__icontains=keyword.lower(), then=Value(3)),
                        When(book__author__name__icontains=keyword.lower(), then=Value(2)),
                        When(book__publisher__name__icontains=keyword.lower(),then=Value(1),),
                        default=Value(0),
                        output_field=IntegerField(),
                    )
                )
                .order_by("-relevance")
            )

        return queryset
