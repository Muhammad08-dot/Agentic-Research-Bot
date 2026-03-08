from duckduckgo_search import DDGS

class WebSearcher:
    def __init__(self):
        self.ddgs = DDGS()

    def search(self, query: str, max_results: int = 10) -> list:
        """Search DuckDuckGo and return results"""
        results = []
        try:
            search_results = self.ddgs.text(
                query,
                max_results=max_results
            )
            for r in search_results:
                results.append({
                    "title": r.get("title", ""),
                    "body": r.get("body", ""),
                    "url": r.get("href", "")
                })
            return results
        except Exception as e:
            print(f"Search error: {e}")
            return []

    def search_news(self, query: str, max_results: int = 5) -> list:
        """Search recent news"""
        results = []
        try:
            news_results = self.ddgs.news(
                query,
                max_results=max_results
            )
            for r in news_results:
                results.append({
                    "title": r.get("title", ""),
                    "body": r.get("body", ""),
                    "url": r.get("url", ""),
                    "date": r.get("date", "")
                })
            return results
        except Exception as e:
            print(f"News search error: {e}")
            return []

    def format_results(self, results: list) -> str:
        """Format search results into readable text"""
        formatted = ""
        for i, r in enumerate(results, 1):
            formatted += f"""
            [{i}] Title: {r['title']}
            Content: {r['body']}
            Source: {r['url']}
            {'Date: ' + r.get('date', '') if r.get('date') else ''}
            {'-'*50}
            """
        return formatted