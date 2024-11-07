from django.http import JsonResponse

from .services.exchange_rate_api_service import get_current_usd_service


def get_current_usd(req) -> JsonResponse:

    data = get_current_usd_service()

    return JsonResponse({"status": "OK", "data": [data]})