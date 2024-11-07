import requests as api_req

from dollar_rate.services.service import add_new_rate, get_last_count_rates
from tracking_dallar_rate import settings


def get_current_usd_service() -> list[dict[str, str]]:
    """Получение нового курса и 10 последних"""
    add_new_rate(api_req.get(settings.EXCHANGE_RATE_API_LINK).json()['conversion_rates']['RUB'])

    rates = get_last_count_rates(11)

    data = []

    for rate in rates:
        data.append({
            "rate": rate.usd_to_rub_rate,
            "date": rate.date_time_request
        })

    return data