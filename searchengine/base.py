import abc
from bs4 import BeautifulSoup


class SearchEngine(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def query(self, query: str) -> BeautifulSoup:
        """every search engine should have query method"""
        pass

    @abc.abstractmethod
    def parser(self, content) -> BeautifulSoup:
        """every search engine should have parser method"""
        pass
