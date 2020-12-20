from database.models import SearchHistory
from searchengine.base import SearchEngine


def search(search_engine: SearchEngine, query: str, top_n: int = 5) -> list:
    html = search_engine.query(query)
    links = []
    if html:
        links = top_n_results(fetch_links(html), top_n)
    return links


def save_search_history(query: str, db_session):
    result = db_session.query(SearchHistory).filter(SearchHistory.query_text == query).first()
    if not result:
        search_history = SearchHistory(query_text=query)
        db_session.add(search_history)
        db_session.commit()


def get_recent_search(query: str, db_session, top_n=10) -> list:
    result_set = db_session.query(SearchHistory).filter(SearchHistory.query_text.like(f"%{query}%")).order_by(
        SearchHistory.timestamp.desc()).limit(top_n)

    recent_search = []
    for row in result_set:
        recent_search.append(row.query_text)
    return recent_search


def fetch_links(html):
    main_div = html.find("div", {'id': "main"})
    if main_div:
        divs = main_div.findAll("div", {"class": "kCrYT"})
        if divs:
            for div in divs:
                a_tag = div.a
                if a_tag:
                    yield a_tag['href']


def top_n_results(results, n: int = 5) -> list:
    top_results = []
    for i, item in enumerate(results):
        if i == n:
            break
        url = f"https://www.google.com/{item}"
        top_results.append(url)

    return top_results
