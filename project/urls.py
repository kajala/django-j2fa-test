from django.urls import path
from django.contrib import admin
from django.urls import reverse_lazy
from django.views.generic import RedirectView
from j2fa.views import TwoFactorAuth

urlpatterns = [
    path('admin/', admin.site.urls),
    path('2fa/', TwoFactorAuth.as_view(), name='j2fa-obtain-auth'),
    path('', RedirectView.as_view(url=reverse_lazy('admin:login'))),
]
