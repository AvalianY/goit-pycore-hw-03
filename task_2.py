import random
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