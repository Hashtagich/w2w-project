from accounts.models import Role
from .support_def import get_json, clear_db


# Create
def create_role_db():
    """Функция для наполнения базы данных Роли из файла role.json"""
    if not Role.objects.count():
        data = get_json(name_json_file='role')
        for db in data:
            Role(
                title=db['name'],
            ).save()


# Delete
def clear_role_db():
    """Функция для удаления базы данных Роли."""
    return clear_db(name_model=Role)
