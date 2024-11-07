from django.contrib import admin

from dollar_rate.models import DollarRateHistory

@admin.register(DollarRateHistory)
class DollarRateHistoryAdmin(admin.ModelAdmin):
    list_display = "usd_to_rub_rate", "date_time_request"
