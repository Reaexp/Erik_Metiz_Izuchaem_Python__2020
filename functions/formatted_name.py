def get_formated_name(first_name, last_name):
    """Возвращает аккуратно отформатированное имя."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formated_name("алекс", "reaexp")
print(musician)