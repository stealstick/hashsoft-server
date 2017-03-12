from rest_framework import viewsets
from .models import Report
from .serializers import ReportSerializer


class ReportViewSet(viewsets.ModelViewSet):
    serializer_class = ReportSerializer
    queryset = Report.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
