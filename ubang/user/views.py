from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework_jwt.views import ObtainJSONWebToken
from rest_framework.mixins import ListModelMixin

from .serializers import UserSerializer
from .models import CustomUser

class LoginJwtTokenView(ObtainJSONWebToken):
    
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        
        if response.status_code == 200:
            context = {
                'code': 20000,
                'data': response.data,
            }
        else:
            context = {
                'code': 20001,
                'message': 'Unable to log in with provided credentials.'
            }
        
        return Response(context)

class LogoutJwtTokenView(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        context = {
            'code': 20000,
            'message': 'ok'
        }
        return Response(context)

class UserInfo(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = UserSerializer(request.user)
        context = {
            'code': 20000,
            'data': {
                'roles': ['editor'],
                'introduction': 'I am a super administrator',
                'avatar': 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif',
                'name': 'Editor',
                'extra': user.data
            }
        }
        return Response(context)

class UserView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    
    filterset_fields = ('is_driver', 'is_tourguide', 'is_actived')
    ordering_fields = ('id', 'username', 'is_driver', 'is_tourguide', 'is_actived')
    search_fields = ('username', 'email')
    ordering = ('id', )
    
    def list(self, request):
        response = super().list(request)
        
        context = {
            'code': 20000,
            'data': response.data,
        }

        return Response(context)

    @action(detail=False, methods=['get'])
    def info(self, request):
        serializer = UserSerializer(request.user)
        context = {
            'code': 20000,
            'data': serializer.data,
        }

        return Response(context)

    def retrieve(self, request, pk=None):
        response = super().retrieve(request, pk)
        
        context = {
            'code': 20000,
            'data': response.data
        }
            
        return Response(context)

    def update(self, request, *args, **kwargs):
        print(request.data)
        try:
            response = super().update(request, *args, **kwargs)
            context = {
                'code': 20000,
                'data': response.data
            }

            return Response(context)
        except (ValueError, Exception) as e:
            context = {
                'code': 20001,
                'message': '%s' % e
            }
                
            return Response(context)