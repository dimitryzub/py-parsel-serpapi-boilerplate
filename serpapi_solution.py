import os, json
from serpapi import GoogleSearch


def serpapi_scrape():
    params = {
        # https://docs.python.org/3/library/os.html#os.getenv
        "api_key": os.getenv("API_KEY"), # your serpapi API key
        "engine": "google_scholar",      # search engine
        "q": "query",                    # search query
        "hl": "en",                      # language
    }
    
    search = GoogleSearch(params)
    results = search.get_dict()
    
