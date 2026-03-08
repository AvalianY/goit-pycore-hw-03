from datetime import date, datetime, timedelta
import random
import re

# Task 1
def get_days_from_today(date_str: str) -> int:
    user_date = datetime.strptime(date_str, "%Y-%m-%d").date()
    return (date.today() - user_date).days

print(get_days_from_today("2025-01-29"))

# Task 2
def get_numbers_ticket(min, max, quantity) -> list:
    if (not isinstance(min, int) or
        not isinstance(max, int) or
        not isinstance(quantity, int) or
        min < 1 or
        max > 1000 or
        min >= max or
        quantity < 1 or
        quantity > (max - min + 1)
    ): return []

    return sorted(random.sample(range(min, max + 1), quantity))

print(get_numbers_ticket(1, 10, 5))

# Task 3
def normalize_phone(phone_number) -> str:
    temp_number = re.sub(r'\D', "", phone_number)
    temp_number = "+" + temp_number if temp_number.startswith("380") else "+38" + temp_number
    return temp_number


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
    ]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)

# Task 4
def get_upcoming_birthdays(users: list[dict[str, str]]) -> list[dict[str, str]]:
    upcoming_birthdays = []
    today = datetime.today().date()

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        delta_days = (birthday_this_year - today).days

        if 0 <= delta_days <= 7:
            congratulation_date = birthday_this_year

            if congratulation_date.weekday() == 5:
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:
                congratulation_date += timedelta(days=1)

            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays


users = [
    {"name": "John Doe", "birthday": "1985.03.16"},
    {"name": "Jane Smith", "birthday": "1990.03.07"},
    {"name": "Will Smit", "birthday": "1985.03.08"},
    {"name": "Hue Lorie", "birthday": "1985.03.23"},
    {"name": "Samuel Jackson", "birthday": "1985.03.02"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)