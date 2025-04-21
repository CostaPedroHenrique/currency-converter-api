from decimal import Decimal

from celery import shared_task

from apps.notifications.models import Notification
from apps.transactions.models import CurrencyAlert
from apps.transactions.services import ConversionService


@shared_task
def check_currency_alerts():
    response = ConversionService.get_conversion_rates()
    rates = response.get("rates", {})

    alerts = CurrencyAlert.objects.filter(is_active=True)

    for alert in alerts:
        source_currency = alert.source_currency
        target_currency = alert.target_currency

        if source_currency not in rates or target_currency not in rates:
            continue

        source_rate = Decimal(str(rates[source_currency]))
        target_rate = Decimal(str(rates[target_currency]))

        base_rate = alert.base_rate
        converted_value = target_rate / source_rate

        diff_percent = ((converted_value - base_rate) / base_rate) * 100

        should_notify = False
        title = ""
        type = ""

        if diff_percent >= alert.variation_threshold:
            title = f"{source_currency} → {target_currency} subiu {diff_percent:.2f}%"
            type = "UP"
            should_notify = True
        elif diff_percent <= -alert.variation_threshold:
            title = (
                f"{source_currency} → {target_currency} caiu {abs(diff_percent):.2f}%"
            )
            type = "DOWN"
            should_notify = True

        if should_notify:
            Notification.objects.create(
                user=alert.user,
                title=title,
                message=(
                    f"A variação do {source_currency} para {target_currency} "
                    f"é agora de {converted_value:.4f}."
                ),
                type=type,
            )

            alert.base_rate = converted_value
            alert.save()
