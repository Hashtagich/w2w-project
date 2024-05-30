from customer.models import customer
from .support_def import get_json, create_simple_db, clear_db


# Create
def create_role_db():
    """Функция для наполнения базы данных Роли пользователя данными из файла role.json"""
    create_simple_db(name_model=customer.Role, name_json_file='role')


def create_tariff_db():
    """Функция для наполнения базы данных Тарифы данными из файла tariff.json"""
    if not customer.Tariff.objects.count():
        data = get_json(name_json_file='tariff')
        for db in data:
            customer.Tariff(
                name=db['name'],
                price=db['price'],
                description=db['description']
            ).save()


def create_customer_db():
    """Функция для наполнения базы данных Пользователи данными из файла customer.json"""
    if not customer.Customer.objects.count():
        data = get_json(name_json_file='customer')
        for db in data:
            customer.Customer(
                name=db['name'],
                surname=db['surname'],
                patronymic=db['patronymic'],
                email=db['email'],
                phone=db['phone'],
                gender=db['gender'],
                status=customer.Role.objects.get(name=db['status']),
                tariff=customer.Tariff.objects.get(name=db['tariff'])
            ).save()


# Delete
def clear_role_db():
    """Функция для удаления базы данных Роли."""
    return clear_db(name_model=customer.Role)


def clear_tariff_db():
    """Функция для удаления базы данных Тарифы."""
    return clear_db(name_model=customer.Tariff)


def clear_customer_db():
    """Функция для удаления базы данных Пользователи."""
    return clear_db(name_model=customer.Customer)
