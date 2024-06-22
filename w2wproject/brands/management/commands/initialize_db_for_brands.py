from django.core.management.base import BaseCommand
from .command_for_other import create_average_check_db, create_number_subscribers_db, create_interests_db, \
    create_predictions_db
from .command_for_social_network import create_name_social_network_db
from .command_for_brand import create_category_db
from .command_for_accounts import create_role_db


class Command(BaseCommand):
    """
    Класс для инициализации баз данных. Каждая база данных создаётся через запуск конкретной функции.
    Подробное описание какая база создаётся и как описано непосредственно в функциях.
    """
    help = '''
    Initialize db 
    Инициализировать баз данных'''

    def handle(self, *args, **options):
        create_number_subscribers_db()
        self.stdout.write(self.style.SUCCESS(
            'Initialize db NumberSubscribers successfully.\nИнициализация базы данных Количества подписчиков выполнена успешно.'))

        create_average_check_db()
        self.stdout.write(self.style.SUCCESS(
            'Initialize db AverageCheck successfully.\nИнициализация базы данных Среднего чека выполнена успешно.'))

        create_interests_db()
        self.stdout.write(self.style.SUCCESS(
            'Initialize db Interest successfully.\nИнициализация базы данных Интересов выполнена успешно.'))

        create_predictions_db()
        self.stdout.write(self.style.SUCCESS(
            'Initialize db Prediction successfully.\nИнициализация базы данных Предсказаний выполнена успешно.'))

        create_name_social_network_db()
        self.stdout.write(self.style.SUCCESS(
            'Initialize db NameSocialNetwork successfully.\nИнициализация базы данных Названия соц сетей выполнена успешно.'))

        create_category_db()
        self.stdout.write(self.style.SUCCESS(
            'Initialize db Category successfully.\nИнициализация базы данных Категории выполнена успешно.'))

        create_role_db()
        self.stdout.write(self.style.SUCCESS(
            'Initialize db Role successfully.\nИнициализация базы данных Роли выполнена успешно.'))

        self.stdout.write(self.style.SUCCESS(
            'Initialize db command executed successfully.\nКоманда инициализации базы данных выполнена успешно.'))
