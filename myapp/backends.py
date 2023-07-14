from django.contrib.auth.backends import BaseBackend

from myapp.UserModel import FizUser, UrUser


class FizUserBackend(BaseBackend):
    def authenticate(self, request, email=None, full_name=None):
        try:
            User = FizUser.objects.get(email=email, full_name=full_name)
        except FizUser.DoesNotExist:
            return None

        return User

    def get_user(self, user_id):
        try:
            return FizUser.objects.get(pk=user_id)
        except FizUser.DoesNotExist:
            return None
class UrUserBackend(BaseBackend):
    def authenticate(self, request, email=None, company_name=None, password=None, **kwargs):
        try:
            User = UrUser.objects.get(email=email, company_name=company_name, password=password)
        except UrUser.DoesNotExist:
            return None

        if User.check_password(password):
            return User

        return None
    def get_user(self, user_id):
        try:
            return UrUser.objects.get(pk=user_id)
        except UrUser.DoesNotExist:
            return None