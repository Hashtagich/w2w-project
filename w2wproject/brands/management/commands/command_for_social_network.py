from brands.models import social_network
from .support_def import create_simple_db, clear_db


# Create

def create_name_social_network_db():
    """Функция для наполнения базы данных Название социальных сетей из файла name_social_network.json"""
    create_simple_db(name_model=social_network.NameSocialNetwork, name_json_file='name_social_network')


# Delete
def clear_name_social_network_db():
    """Функция для удаления базы данных Название социальных сетей."""
    return clear_db(name_model=social_network.NameSocialNetwork)
