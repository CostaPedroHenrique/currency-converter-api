from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken


class GoogleLoginView(SocialLoginView):
    authentication_classes = []
    adapter_class = GoogleOAuth2Adapter
    # callback_url = "http://localhost:3000"
    client_class = OAuth2Client

    def get_response(self):
        # Gera os tokens (refresh e access)
        refresh = RefreshToken.for_user(self.user)

        return Response(
            {
                "access": str(refresh.access_token),
                "refresh": str(refresh),
            }
        )
