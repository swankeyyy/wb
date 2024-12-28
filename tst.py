import requests
import asyncio


headers = {
    "Accept": "*/*",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "Connection": "keep-alive",
    "Origin": "https://www.wildberries.by",
    "Referer": "https://www.wildberries.by/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
    "sec-ch-ua": 'Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "macOS",
}


def prepare_url(article: str, basket_number: int) -> str:
    """Takes article and basket_number(for iterator) and returns url string"""
    vol: str = f"vol{article[:4]}"
    part: str = f"part{article[:6]}"
    url: str = f"https://basket-{basket_number}.wbbasket.ru/{vol}/{part}/{article}/info/ru/card.json"
    return url


async def get_by_article(article: str):
    """Takes article and search content by basket_numbers"""
    for basket_number in range(10, 20):
        url: str = prepare_url(article, basket_number)
        response = requests.get(url=url, headers=headers)
        if response.status_code == 200:
            print(response.json())
            break


asyncio.run(get_by_article("277990507"))
