import re


def validate_phone_number(phone):
    """
    Проверяет, соответствует ли номер телефона формату +7-800-555-35-35.
    :param phone: Строка, представляющая номер телефона.
    :return: True, если номер соответствует формату, иначе False.
    """
    pattern = r'^\+7-\d{3}-\d{3}-\d{2}-\d{2}$'
    return bool(re.match(pattern, phone))
