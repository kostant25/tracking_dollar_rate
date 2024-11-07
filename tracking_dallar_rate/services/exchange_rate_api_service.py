import requests as api_req
from datetime import datetime

from tracking_dallar_rate import settings


def get_current_usd_service() -> dict[str, str]:
    data = {
        'rate': api_req.get(settings.EXCHANGE_RATE_API_LINK).json()['conversion_rates']['RUB'],
        'time': datetime.now().strftime('%m/%d/%Y %H:%M:%S'),
    }
    return data