from django.core.management.base import BaseCommand
from .command_for_customer import create_role_db, create_tariff_db, create_customer_db


class Command(BaseCommand):
    """
    Класс для инициализации баз данных. Каждая база данных создаётся через запуск конкретной функции.
    Подробное описание какая база создаётся и как описано непосредственно в функциях.
    """
    help = '''
    Initialize db 
    Инициализировать баз данных'''

    def handle(self, *args, **options):
        create_role_db()
        self.stdout.write(self.style.SUCCESS(
            'Initialize db Role successfully.\nИнициализация базы данных Ролей пользователей выполнена успешно.'))

        create_tariff_db()
        self.stdout.write(self.style.SUCCESS(
            'Initialize db Tariff successfully.\nИнициализация базы данных Тарифов выполнена успешно.'))

        create_customer_db()
        self.stdout.write(self.style.SUCCESS(
            'Initialize db Customer successfully.\nИнициализация базы данных Пользователи выполнена успешно.'))

        self.stdout.write(self.style.SUCCESS(
            'Initialize db command executed successfully.\nКоманда инициализации базы данных выполнена успешно.'))
