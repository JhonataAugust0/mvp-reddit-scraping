import praw
from ..domain.ports.reddit_scraper_port import RedditScraperPort
import hashlib
import re

class RedditPrawAdapter(RedditScraperPort):
    def __init__(self, client_id, client_secret, user_agent):
        self.reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent=user_agent,
        )

    def anonymize_author(self, author_name):
        """Substitui o nome do autor por um hash ou 'Anônimo'."""
        if author_name:
            return hashlib.sha256(author_name.encode()).hexdigest()
        return 'Anônimo'

    def anonymize_text(self, text):
        """Remove URLs e substitui informações identificáveis."""
        text = re.sub(r'http\S+', '[URL]', text)
        return text
    
    def process_item(self, item, item_type='Post'):
        """Função recursiva para processar e anonimizar post e comentários."""
        anon_author = self.anonymize_author(item.author.name if item.author else None)
        anon_text = self.anonymize_text(item.selftext if item_type == 'Post' else item.body)

        item_data = {
            'Type': item_type,
            'Post_id': item.id,
            'Title': self.anonymize_text(item.title if item_type == 'Post' else item.submission.title),
            'Author': anon_author,
            'Timestamp': item.created_utc,
            'Text': anon_text,
            'Score': item.score,
            'Total_comments': item.num_comments if item_type == 'Post' else 0,
            'Post_URL': '[REDACTED]' if item_type == 'Post' else None
        }

        return item_data


    def fetch_top_posts(self, subreddit_name, limit=10):
        subreddit = self.reddit.subreddit(subreddit_name)
        data = []

        for post in subreddit.top(limit=limit):
            data.append(self.process_item(post, item_type='Post'))

            # Processar os comentários do post
            post.comments.replace_more(limit=5)
            for comment in post.comments.list():
                data.append(self.process_item(comment, item_type='Comment'))

        return data
