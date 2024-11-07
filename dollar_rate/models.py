from django.db import models

class DollarRateHistory(models.Model):
    usd_to_rub_rate = models.FloatField()
    date_time_request = models.DateTimeField()