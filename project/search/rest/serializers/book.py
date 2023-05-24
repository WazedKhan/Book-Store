from rest_framework.serializers import ModelSerializer

from author.rest.serializer.author import SlimAuthorSerializer

from publisher.rest.serializers.publisher import SlimPublisherSerializer

from book.models import Book


class SearchBooksSerializer(ModelSerializer):
    author = SlimAuthorSerializer()
    publisher = SlimPublisherSerializer()

    class Meta:
        model = Book
        fields = ["id", "name", "pages", "price", "author", "publisher"]
