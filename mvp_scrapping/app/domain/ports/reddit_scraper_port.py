from abc import ABC, abstractmethod


class RedditScraperPort(ABC):
    @abstractmethod
    def fetch_top_posts(self, subreddit, limit):
        """Deve retornar os posts do subreddit"""
        pass
