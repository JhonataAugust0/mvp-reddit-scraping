class RedditScraper:
    def __init__(self, reddit_adapter):
        self.reddit_adapter = reddit_adapter

    def get_top_posts(self, subreddit: str, limit: int = 10) -> dict:
        """Usa o adaptador externo para obter os posts do Reddit"""
        return self.reddit_adapter.fetch_top_posts(subreddit, limit)
