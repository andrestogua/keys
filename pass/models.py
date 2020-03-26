from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PassModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account = models.CharField(verbose_name="Cuenta", max_length=50)
    password = models.CharField(verbose_name="Contraseña", max_length=50)

    class Meta:
        verbose_name = "Contraseña"
        verbose_name_plural = "Contraseñas"

    def __str__(self):
        return '{}'.format(self.account)

    def save(self):
        self.account = self.account.upper()
        super(PassModel,self).save()
    