import os

import pytest
from unittest.mock import MagicMock
from mvp_scrapping.app.adapters.reddit_praw_adapter import RedditPrawAdapter


@pytest.fixture
def praw_mock():
    # Mock PRAW
    reddit = MagicMock()
    subreddit = MagicMock()
    post = MagicMock()
    
    # Mock dos métodos e atributos
    reddit.subreddit.return_value = subreddit
    subreddit.top.return_value = [post]
    post.id = "post_id"
    post.title = "Sample Title"
    post.author.name = "author_name"
    post.selftext = "Sample text with http://example.com"
    post.score = 100
    post.num_comments = 10
    post.comments.replace_more = MagicMock()
    post.comments.list.return_value = []
    
    return reddit

def test_fetch_top_posts(praw_mock):
    # Instancia o adaptador com o mock
    adapter = RedditPrawAdapter(client_id=os.getenv("CLIENT_ID"), client_secret=os.getenv("CLIENT_SECRET"), user_agent=os.getenv("CLIENT_AGENT"))
    adapter.reddit = praw_mock  

    posts = adapter.fetch_top_posts("fitness", limit=1)
    
    assert len(posts) == 1
    assert posts[0]['Title'] == "Sample Title"
    assert posts[0]['Author'] != "author_name"  # Autor deve estar anonimizado
    assert posts[0]['Post_URL'] == "[REDACTED]"
