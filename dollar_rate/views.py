from datetime import datetime, timedelta

from django.http import JsonResponse
from django.core.cache import cache

from .services.exchange_rate_api_service import get_current_usd_service
from .services.get_ip import get_client_ip


def get_current_usd(req) -> JsonResponse:
    """Получение текущего курса и последних 10 запросов"""
    client_ip = get_client_ip(req)
    data = []

    if not cache.get(client_ip):
        cache.set(client_ip, datetime.now())
        data = get_current_usd_service()
    elif cache.get(client_ip) <= datetime.now() - timedelta(seconds=15):
        cache.set(client_ip, datetime.now())
        data = get_current_usd_service()
    else:
        data = [{"message": "Try again latter"}]

    return JsonResponse({"status": "OK", "data": data})
