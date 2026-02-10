import requests
from app.search.provider import SearchProvider

class DuckDuckGoSearchProvider(SearchProvider):
    def search(self, query: str):
        url = "https://api.duckduckgo.com/"
        params = { "q": query, "format": "json", "no_html": "1", "skip_disambig": "1" }

        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        results = []

        for item in data.get("RelatedTopics", [])[:5]:
            if isinstance(item, dict) and "Text" in item:
                results.append({
                    "title": item["Text"][:60],
                    "snippet": item["Text"],
                    "url": item.get("FirstURL", ""),
                })

        return results
