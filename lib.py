def calculate_discount(price: float, discount_percent: float) -> float:
    """
    Розраховує підсумкову вартість товару з урахуванням знижки.
    """
    if price < 0 or discount_percent < 0:
        return 0.0
    return price * (1 - discount_percent / 100)


def format_user_name(name: str, surname: str) -> str:
    """
    Форматує ім'я та прізвище у стандартний вигляд (Прізвище, Ім'я).
    """
    return f"{surname.strip().capitalize()}, {name.strip().capitalize()}"