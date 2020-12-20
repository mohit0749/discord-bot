from requests.exceptions import RequestException


class SearchEngineError(RequestException):
    """A error occurred when querying search engine"""
    pass
