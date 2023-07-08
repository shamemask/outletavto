from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class Meta:
        app_label = 'myapp'

    email = models.EmailField(unique=True)
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='myapp_user_groups'  # Измененное related_name
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='myapp_user_permissions'  # Измененное related_name
    )
    shop_name = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    promo_code = models.CharField(max_length=255)
    terms_of_service = models.BooleanField()
    city = models.CharField(max_length=255)
    shop_name2 = models.CharField(max_length=255)
    form = models.CharField(max_length=255)
    organization_name = models.CharField(max_length=255)
    legal_address = models.CharField(max_length=255)
    inn = models.CharField(max_length=12)
    kpp = models.CharField(max_length=9)
    bank = models.CharField(max_length=255)
    bik = models.CharField(max_length=9)
    account_number = models.CharField(max_length=20)
    correspondent_account = models.CharField(max_length=20)

    def __str__(self):
        return self.username