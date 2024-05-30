from django.core.management.base import BaseCommand
from .command_for_customer import clear_role_db, clear_tariff_db, clear_customer_db


class Command(BaseCommand):
    """
    Класс для инициализации баз данных. Каждая база данных создаётся через запуск конкретной функции.
    Подробное описание какая база создаётся и как описано непосредственно в функциях.
    """
    help = '''
    Initialize db 
    Инициализировать базы данных'''

    def handle(self, *args, **options):
        count = clear_customer_db()
        self.stdout.write(self.style.SUCCESS(
            f'{count} records deleted from the database.\nЗаписи Customer в количестве {count} шт. удалены из базы данных.'))

        count = clear_role_db()
        self.stdout.write(self.style.SUCCESS(
            f'{count} records deleted from the database.\nЗаписи Role в количестве {count} шт. удалены из базы данных.'))

        count = clear_tariff_db()
        self.stdout.write(self.style.SUCCESS(
            f'{count} records deleted from the database.\nЗаписи Tariff в количестве {count} шт. удалены из базы данных.'))

        # End
        self.stdout.write(self.style.SUCCESS(
            'Initialize db command executed successfully.\nКоманда инициализации базы данных выполнена успешно.'))
