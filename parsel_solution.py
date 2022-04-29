from parsel import Selector
import requests, json, os


def parsel_scrape():
    # https://docs.python-requests.org/en/master/user/quickstart/#passing-parameters-in-urls
    params = {
        "q": "query",  # search query
        "hl": "en",                              # language of the search
        "gl": "us"                               # country of the search
    }
    
    # https://docs.python-requests.org/en/master/user/quickstart/#custom-headers
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
    }

    html = requests.get("https://scholar.google.com/scholar", params=params, headers=headers, timeout=30)
    selector = Selector(html.text)
