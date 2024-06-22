from news.models import Post
from .support_def import get_json, clear_db


# Create
def create_news_db():
    """Функция для наполнения базы данных Новости из файла news.json"""
    if not Post.objects.count():
        data = get_json(name_json_file='news')
        for db in data:
            Post(
                title=db['title'],
                text=db['text'],
                link=db['link'],
            ).save()


# Delete
def clear_news_db():
    """Функция для удаления базы данных Новости."""
    return clear_db(name_model=Post)
