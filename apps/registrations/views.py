from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets

from .models import Registration
from .serializers import RegistrationReadSerializer, RegistrationWriteSerializer


class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ["created_at"]
    filterset_fields = ["parent_checklist__id", "process_number", "company"]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return RegistrationReadSerializer
        return RegistrationWriteSerializer
