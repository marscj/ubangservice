from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Brand, Model, Vehicle, ModelPrice
from .serializers import VehicleSerializer, ModelSerializer

class VehicleView(ModelViewSet):
    permission_classes = [IsAuthenticated]

    filterset_fields = ('model', )

    search_fields = ('model__passengers',)

    def get_serializer_class(self):
        if self.action == 'list':
            return VehicleSerializer
        else :
            return VehicleSerializer

    def get_queryset(self):

        return Vehicle.objects.all()

    def list(self, request):
        try:
            response = super().list(request)

            context = {
                'code': 20000,
                'data': response.data,
            }
            
            return Response(context)
        except (ValueError, Exception) as e:
            context = {
                'code': 20001,
                'message': '%s' % e
            }
            return Response(context)

class VehicleModelView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ModelSerializer
    queryset = Model.objects.all()

    def list(self, request):
        try:
            response = super().list(request)

            context = {
                'code': 20000,
                'data': response.data,
            }
            
            return Response(context)
        except (ValueError, Exception) as e:
            context = {
                'code': 20001,
                'message': '%s' % e
            }
            return Response(context)