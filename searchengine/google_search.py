from searchengine.base import SearchEngine
from errors.exceptions import SearchEngineError
from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin


class Google(SearchEngine):
    def __init__(self, host: str, path: str = "search", query_params: str = "q"):
        self.url = urljoin(host, path)
        self.query_params = query_params

    def query(self, query: str) -> BeautifulSoup:
        get = requests.get(self.url, params=f"q={query}")
        if get.status_code >= 400:
            raise SearchEngineError
        return self.parser(get.content)

    def parser(self, content) -> BeautifulSoup:
        return BeautifulSoup(content, "lxml")
