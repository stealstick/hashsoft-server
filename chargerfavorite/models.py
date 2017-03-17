from django.db import models

from accounts.models import User
from chargers.models import Charger


class ChargerFavorite(models.Model):
    user = models.ForeignKey(User, related_name="charger_favorites")
    charger = models.ForeignKey(Charger, related_name="charger_favorites")
