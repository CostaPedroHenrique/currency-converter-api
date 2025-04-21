from apps.transactions.tasks import check_currency_alerts


def check_currency_alerts_cron():
    """
    Test the check_currency_alerts function.
    """
    check_currency_alerts()
