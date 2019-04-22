from django.db import models
from django.utils.translation import ugettext_lazy as _

class Itinerary(models.Model):
    
    name = models.CharField(max_length=128, unique=True)
    is_fullday = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("Itinerary")
        verbose_name_plural = _("Itineraries")

    def __str__(self):
        return self.name