from brands.models import brand
from .support_def import get_json, create_simple_db, clear_db


# Create
def create_category_db():
    """Функция для наполнения базы данных Категории из файла category.json"""
    create_simple_db(name_model=brand.Category, name_json_file='category')


# Delete
def clear_category_db():
    """Функция для удаления базы данных Категории."""
    return clear_db(name_model=brand.Category)
