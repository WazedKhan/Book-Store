from rest_framework.serializers import ModelSerializer

from ...models import Author


class SlimAuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ["id", "name", "age"]
