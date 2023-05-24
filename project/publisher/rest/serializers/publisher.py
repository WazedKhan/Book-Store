from rest_framework import serializers

from ...models import Publisher


class SlimPublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ["id", "name"]
