from customer.models import customer
import json


# Support
def get_json(name_json_file):
    """Вспомогательная функция для открытия json файла и передачи его содержимого."""
    with open(f"files_for_filling_db/{name_json_file}.json", "r", encoding='utf-8') as file:
        result_data = json.load(file)
        return result_data


# Create
def create_role_db():
    """Функция для наполнения базы данных Роли пользователя данными из файла role.json"""
    if not customer.Role.objects.count():
        data = get_json(name_json_file='role')
        for db in data:
            customer.Role(
                name=db['name']
            ).save()


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
def clear_db(name_model) -> int:
    """Общая функция для удаления базы данных нужно только ввести название модели name_model в качестве аргумента."""
    count = name_model.objects.count()
    name_model.objects.all().delete()
    return count


def clear_role_db():
    """Функция для удаления базы данных Роли."""
    return clear_db(name_model=customer.Role)


def clear_tariff_db():
    """Функция для удаления базы данных Тарифы."""
    return clear_db(name_model=customer.Tariff)


def clear_customer_db():
    """Функция для удаления базы данных Пользователи."""
    return clear_db(name_model=customer.Customer)
