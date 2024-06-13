from django.core.management.base import BaseCommand
from .command_for_customer import clear_role_db, clear_tariff_db, clear_customer_db
from .command_for_other import clear_faq_db, clear_average_check_db, clear_number_subscribers_db, clear_interests_db, \
    clear_predictions_db
from .command_for_social_network import clear_name_social_network_db
from .command_for_brand import clear_category_db


class Command(BaseCommand):
    """
    Класс для инициализации баз данных. Каждая база данных создаётся через запуск конкретной функции.
    Подробное описание какая база создаётся и как описано непосредственно в функциях.
    """
    help = '''
    Initialize db 
    Инициализировать базы данных'''

    def handle(self, *args, **options):
        # count = clear_customer_db()
        # self.stdout.write(self.style.SUCCESS(
        #     f'{count} records deleted from the database.\nЗаписи Customer в количестве {count} шт. удалены из базы данных.'))

        count = clear_role_db()
        self.stdout.write(self.style.SUCCESS(
            f'{count} records deleted from the database.\nЗаписи Role в количестве {count} шт. удалены из базы данных.'))

        count = clear_tariff_db()
        self.stdout.write(self.style.SUCCESS(
            f'{count} records deleted from the database.\nЗаписи Tariff в количестве {count} шт. удалены из базы данных.'))

        count = clear_faq_db()
        self.stdout.write(self.style.SUCCESS(
            f'{count} records deleted from the database.\nЗаписи FAQ в количестве {count} шт. удалены из базы данных.'))

        count = clear_average_check_db()
        self.stdout.write(self.style.SUCCESS(
            f'{count} records deleted from the database.\nЗаписи Среднего чека в количестве {count} шт. удалены из базы данных.'))

        count = clear_number_subscribers_db()
        self.stdout.write(self.style.SUCCESS(
            f'{count} records deleted from the database.\nЗаписи Количества подписчиков в количестве {count} шт. удалены из базы данных.'))

        count = clear_interests_db()
        self.stdout.write(self.style.SUCCESS(
            f'{count} records deleted from the database.\nЗаписи Интересов в количестве {count} шт. удалены из базы данных.'))

        count = clear_predictions_db()
        self.stdout.write(self.style.SUCCESS(
            f'{count} records deleted from the database.\nЗаписи Предсказаний в количестве {count} шт. удалены из базы данных.'))

        count = clear_name_social_network_db()
        self.stdout.write(self.style.SUCCESS(
            f'{count} records deleted from the database.\nЗаписи Названия соцсетей в количестве {count} шт. удалены из базы данных.'))

        count = clear_category_db()
        self.stdout.write(self.style.SUCCESS(
            f'{count} records deleted from the database.\nЗаписи Категории в количестве {count} шт. удалены из базы данных.'))

        # End
        self.stdout.write(self.style.SUCCESS(
            'Initialize db command executed successfully.\nКоманда инициализации базы данных выполнена успешно.'))
