import os

from adapters.reddit_praw_adapter import RedditPrawAdapter
from adapters.storage_adapter import StorageAdapter
from domain.reddit_scraper import RedditScraper
from dotenv import load_dotenv

load_dotenv()


def main():
    reddit_adapter = RedditPrawAdapter(
        client_id=os.getenv('CLIENT_ID'),
        client_secret=os.getenv('CLIENT_SECRET'),
        user_agent=os.getenv('CLIENT_AGENT'),
    )
    storage_adapter = StorageAdapter()
    reddit_scraper = RedditScraper(reddit_adapter)

    # Busca os dados de posts
    posts = reddit_scraper.get_top_posts(subreddit='skeptic', limit=10)

    storage = StorageAdapter()
    storage.save_to_csv(posts, 'reddit_skeptic_posts.csv')
    storage.save_to_json(posts, 'reddit_skeptic_posts.json')


if __name__ == "__main__":
    main()
