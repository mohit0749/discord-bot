from searchengine.base import SearchEngine
from errors.exceptions import SearchEngineError
from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin


class Google(SearchEngine):
    """
    Google search engire extends the search engine class.
    It search over www.google.com to fetch results.
    """

    def __init__(self, host: str, path: str = "search", query_params: str = "q"):
        self.url = urljoin(host, path)
        self.query_params = query_params

    def query(self, query: str) -> BeautifulSoup:
        """send the http request to google.com to get the results"""
        get = requests.get(self.url, params=f"q={query}")
        if get.status_code >= 400:
            raise SearchEngineError
        return self.parser(get.content)

    def parser(self, content) -> BeautifulSoup:
        """parses the raw string response to object"""
        return BeautifulSoup(content, "lxml")
