from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView

from myapp.models.User import User


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'account/dashboard.html'
    context_object_name = 'user'
