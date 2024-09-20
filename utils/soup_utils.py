from bs4 import BeautifulSoup
import requests
from utils.url_utils import get_url


def get_soup(url: str, section_name: str) -> BeautifulSoup:
    url = get_url(url, section_name)
    page = requests.get(url)
    return BeautifulSoup(page.content, 'html.parser')
