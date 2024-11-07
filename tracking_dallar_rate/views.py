from django.http import JsonResponse

def get_current_usd(req) -> JsonResponse:
    return JsonResponse({"status": "OK"})