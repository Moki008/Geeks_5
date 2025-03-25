import random
import string

from django.contrib.auth.models import User
from django.db import models


class Code(models.Model):

    code = models.CharField(max_length=6 , unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}:{self.code}"

    @staticmethod
    def generate_code():
        return ''.join(random.choices(string.digits, k=6))

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = self.generate_code()
        super().save(*args, **kwargs)


