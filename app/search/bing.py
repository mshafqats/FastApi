import requests
from app.core.config import settings
from app.search.provider import SearchProvider

class BingSearchProvider(SearchProvider):
    def search(self, query: str):
        url = "https://api.bing.microsoft.com/v7.0/search"
        headers = { "Ocp-Apim-Subscription-Key": settings.BING_API_KEY }
        params = { "q": query, "count": 5, "textDecorations": False, "textFormat": "Raw" }

        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()

        data = response.json()
        results = []

        for item in data.get("webPages", {}).get("value", []):
            results.append({ "title": item["name"], "snippet": item["snippet"], "url": item["url"] })

        return results
