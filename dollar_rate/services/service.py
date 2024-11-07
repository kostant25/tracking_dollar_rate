from dollar_rate.models import DollarRateHistory


def add_new_rate(rate):
    """Создание нового курса"""
    DollarRateHistory.objects.create(usd_to_rub_rate=float(rate))


def get_all_rates():
    """Получение всех запросов курса"""
    return DollarRateHistory.objects.all()[::-1]


def get_last_count_rates(count):
    """Получение count курсов"""
    rates = get_all_rates()
    return rates[:count]