from django.urls import path

from search.rest.views import book


urlpatterns = [path("", book.SearchBooksList.as_view(), name="search-books")]
