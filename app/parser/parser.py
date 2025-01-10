import requests
import asyncio
from app.parser.models import Item
from app.settings import settings

headers: str = settings.PARSER_HEADERS


class ItemParse:
    """Takes an article and parse wb backend"""

    def __init__(self, article: str) -> None:
        self.article = article
        self.headers = headers

    def __prepare_url(self, basket_number: int) -> str:
        """Takes article and basket_number(for iterator) and returns url string"""
        vol: str = f"vol{self.article[:4]}"
        part: str = f"part{self.article[:6]}"
        url: str = (
            f"https://basket-{basket_number}.wbbasket.ru/{vol}/{part}/{self.article}/info/ru/card.json"
        )
        return url

    def get_by_article(self) -> Item:
        """Takes article and search content by basket_numbers"""
        for basket_number in range(10, 20):
            url: str = self.__prepare_url(basket_number)
            response = requests.get(url=url, headers=self.headers)
            if response.status_code == 200:
                result = Item.model_validate(response.json())
                print(result)
                return result.model_dump()
        return None


# asyncio.run(ItemParse("277990507").get_by_article())
