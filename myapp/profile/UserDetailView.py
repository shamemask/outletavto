from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView

from authentication.UserModel import FizUser, UrUser


class FizUserDetailView(LoginRequiredMixin, DetailView):
    model = FizUser
    template_name = 'account/dashboard.html'
    context_object_name = 'user'
class UrUserDetailView(LoginRequiredMixin, DetailView):
    model = UrUser
    template_name = 'account/dashboard.html'
    context_object_name = 'user'
