from customer.models import other
from .support_def import get_json, create_simple_db, clear_db


# Create
def create_faq_db():
    """Функция для наполнения базы данных FAQ данными из файла FAQ.json"""
    if not other.FAQ.objects.count():
        data = get_json(name_json_file='FAQ')
        for db in data:
            other.FAQ(
                question=db['question'],
                answer=db['answer']
            ).save()


def create_average_check_db():
    """Функция для наполнения базы данных Среднего чека данными из файла average_check.json"""
    create_simple_db(name_model=other.AverageCheck, name_json_file='average_check')


def create_number_subscribers_db():
    """Функция для наполнения базы данных Количества подписчиков данными из файла number_subscribers.json"""
    create_simple_db(name_model=other.NumberSubscribers, name_json_file='number_subscribers')


def create_interests_db():
    """Функция для наполнения базы данных Интересов данными из файла interests.json"""
    create_simple_db(name_model=other.Interests, name_json_file='interests')


# Delete
def clear_faq_db():
    """Функция для удаления базы данных FAQ."""
    return clear_db(name_model=other.FAQ)


def clear_average_check_db():
    """Функция для удаления базы данных Среднего чека."""
    return clear_db(name_model=other.AverageCheck)


def clear_number_subscribers_db():
    """Функция для удаления базы данных Количества подписчиков."""
    return clear_db(name_model=other.NumberSubscribers)


def clear_interests_db():
    """Функция для удаления базы данных Интересов."""
    return clear_db(name_model=other.Interests)
