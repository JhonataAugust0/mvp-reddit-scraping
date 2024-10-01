from abc import ABC, abstractmethod


class RedditScraperPort(ABC):
    @abstractmethod
    def anonymize_author(self, author_name: str) -> str:
        """Deve anonimizar o autor da publicação"""
        pass

    @abstractmethod
    def anonymize_text(self, text: str) -> str:
        """Deve substituir informações identificáveis."""
        pass

    @abstractmethod
    def process_item(self, item: any, item_type='Post') -> dict:
        """Deve processar os dados obtidos."""
        pass

    @abstractmethod
    def fetch_top_posts(self, subreddit: str, limit: int) -> dict:
        """Deve retornar os posts do subreddit"""
        pass
