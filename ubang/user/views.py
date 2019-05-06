from rest_framework import views, permissions,status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_jwt import views as jwt_views
# from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response

# from rest_framework.authtoken.models import Token
# from rest_framework.authentication import TokenAuthentication
# from rest_framework_jwt.views import ObtainJSONWebToken
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .serializers import UserSerializer

class LoginAuthTokenView(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})

        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            
            context = {
                'code': 20000,
                'data': token.key
            }
            return Response(context)
        
        else:
            context = {
                'code': 20001,
                'message': 'Unable to log in with provided credentials.'
            }
            return Response(context)

class LoginJwtTokenView(jwt_views.ObtainJSONWebToken):
    
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

class LogoutAuthTokenView(views.APIView):
    
    
    def post(self, request, *args, **kwargs):
        
        # request.user.auth_token.delete()
        
        context = {
            'code': 20000,
            'message': 'ok'
        }

        return Response(context)

class LogoutJwtTokenView(views.APIView):
    
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        
        print(request.headers)
        
        context = {
            'code': 20000,
            'message': 'ok'
        }

        return Response(context)

class UserInfo(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    # renderer_classes = (renderers.JSONRenderer,)
    # serializer_class = UserSerializer

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
        print(context)
        return Response(context)