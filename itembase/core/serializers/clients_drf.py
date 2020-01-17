from rest_framework import serializers

from itembase.core.models import Client


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = (
            'client_code',
            'client_name',
        )


class ClientCodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = (
            'client_code',
        )
