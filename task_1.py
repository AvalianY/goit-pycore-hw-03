from datetime import date, datetime, timedelta
# Task 1
def get_days_from_today(date_str: str) -> int | None:
    try:
        user_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        return (date.today() - user_date).days
    except ValueError:
        print("Неправильний формат дати. Використовуйте формат YYYY-MM-DD.")
        return None

print(get_days_from_today("2025-01-29"))