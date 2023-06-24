from django.urls import path, include

app_name = "book"

urlpatterns = [
    path("book", include("search.rest.urls.book")),
]