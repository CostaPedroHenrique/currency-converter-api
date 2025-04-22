"""
URL configuration for currencyConverter project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.notifications.viewsets import NotificationViewSet
from apps.transactions.viewsets import CurrencyAlertViewSet, TransactionViewSet
from apps.users.views import GoogleLoginView

router = DefaultRouter()
router.register(
    r"transactions",
    TransactionViewSet,
    basename="transaction",
)

router.register(
    r"currency-alerts",
    CurrencyAlertViewSet,
    basename="currency-alert",
)

router.register(
    r"notifications",
    NotificationViewSet,
    basename="notification",
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("api/", include(router.urls)),
    path("api/google-login/", GoogleLoginView.as_view(), name="google_login"),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
]
