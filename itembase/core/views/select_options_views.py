# from braces.views import LoginRequiredMixin, SuperuserRequiredMixin, StaffuserRequiredMixin

from rest_framework.generics import ListAPIView
from itembase.core.models import EngagementType
from itembase.core.serializers.select_options_drf import EngagementTypeSerializer


class EngagementTypeListAPI(ListAPIView):
    queryset = EngagementType.objects.all().order_by('service_abbreviation')
    serializer_class = EngagementTypeSerializer
