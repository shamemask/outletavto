from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from drf_yasg.utils import swagger_auto_schema

from authentication.UserModel import FizUser, UrUser


class FizUserDetailView(LoginRequiredMixin, DetailView):
    model = FizUser
    template_name = 'account/dashboard.html'
    context_object_name = 'user'

    @swagger_auto_schema(
        operation_description="Get FizUser details",
        responses={200: "OK - FizUser details"},
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
class UrUserDetailView(LoginRequiredMixin, DetailView):
    model = UrUser
    template_name = 'account/dashboard.html'
    context_object_name = 'user'

    @swagger_auto_schema(
        operation_description="Get UrUser details",
        responses={200: "OK - UrUser details"},
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
