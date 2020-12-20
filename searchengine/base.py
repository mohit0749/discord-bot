import abc
from bs4 import BeautifulSoup


class SearchEngine(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def query(self, query: str) -> BeautifulSoup:
        pass

    @abc.abstractmethod
    def parser(self, content) -> BeautifulSoup:
        pass
