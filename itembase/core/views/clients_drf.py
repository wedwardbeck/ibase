from rest_framework import viewsets
from itembase.core.serializers.clients_drf import ClientSerializer, ClientCodeSerializer
from itembase.core.models import Client


class ClientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows clients to be viewed or edited.
    """
    queryset = Client.objects.all().order_by('-client_code')
    serializer_class = ClientSerializer


class ClientCodeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows clients to be viewed or edited.
    """
    queryset = Client.objects.all().order_by('-client_code')
    serializer_class = ClientCodeSerializer
