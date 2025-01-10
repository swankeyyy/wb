from celery_config import celery_app
from app.parser.parser import ItemParse
from app.settings import settings
import asyncio


@celery_app.task
def parser_task(article: str):
    """Takes article and search content by basket_numbers"""
    
    item = ItemParse(article=article)
    result = item.get_by_article()
    
    return result
