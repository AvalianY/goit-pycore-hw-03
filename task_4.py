from datetime import datetime, timedelta
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