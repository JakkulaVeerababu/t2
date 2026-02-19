from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Vessel, VesselPosition
from .serializers import VesselSerializer, VesselPositionSerializer
from .services import MockAISProvider

class VesselViewSet(viewsets.ModelViewSet):
    queryset = Vessel.objects.all()
    serializer_class = VesselSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Vessel.objects.all()
        v_type = self.request.query_params.get('type', None)
        flag = self.request.query_params.get('flag', None)
        search = self.request.query_params.get('search', None)
        
        if v_type:
            queryset = queryset.filter(vessel_type=v_type)
        if flag:
            queryset = queryset.filter(flag=flag)
        if search:
            queryset = queryset.filter(name__icontains=search)
            
        return queryset

    @action(detail=False, methods=['post'])
    def sync_mock_data(self, request):
        """Force trigger mock data generation"""
        provider = MockAISProvider()
        positions = provider.generate_positions()
        return Response({'message': f'Updated {len(positions)} vessels'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'])
    def history(self, request, pk=None):
        vessel = self.get_object()
        positions = vessel.positions.all().order_by('-timestamp')[:100]
        serializer = VesselPositionSerializer(positions, many=True)
        return Response(serializer.data)
