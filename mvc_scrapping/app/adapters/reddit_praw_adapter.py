import praw
from domain.ports.reddit_scraper_port import RedditScraperPort


class RedditPrawAdapter(RedditScraperPort):
    def __init__(self, client_id, client_secret, user_agent):
        self.reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent=user_agent,
        )

    def fetch_top_posts(self, subreddit_name, limit=10):
        subreddit = self.reddit.subreddit(subreddit_name)
        posts = []
        for post in subreddit.top(limit=limit):
            posts.append(
                {
                    'Type': 'Post',
                    'Post_id': post.id,
                    'Title': post.title,
                    'Author': post.author.name if post.author else 'Unknown',
                    'Timestamp': post.created_utc,
                    'Text': post.selftext,
                    'Score': post.score,
                    'Total_comments': post.num_comments,
                    'Post_URL': post.url,
                }
            )

            # Se quiser incluir comentários
            if post.num_comments > 0:
                post.comments.replace_more(limit=5)
                for comment in post.comments.list():
                    posts.append(
                        {
                            'Type': 'Comment',
                            'Post_id': post.id,
                            'Title': post.title,
                            'Author': comment.author.name
                            if comment.author
                            else 'Unknown',
                            'Timestamp': comment.created_utc,
                            'Text': comment.body,
                            'Score': comment.score,
                        }
                    )
        return posts
