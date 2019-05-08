from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator

from decimal import Decimal

class Discount(models.Model):
    
    name = models.CharField(max_length=128)
    value = models.DecimalField(default=Decimal(0.0), max_digits=3, decimal_places=2, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])

    class Meta:
        verbose_name = _("Disscount")
        verbose_name_plural = _("Disscounts")

    def __str__(self):
        return self.name