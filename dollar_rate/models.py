from django.db import models

class DollarRateHistory(models.Model):
    usd_to_rub_rate = models.FloatField()
    date_time_request = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.date_time_request)

    class Meta:
        verbose_name = 'Dollar Rate'