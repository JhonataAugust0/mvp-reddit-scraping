import os

from mvp_scrapping.app.adapters.reddit_praw_adapter import RedditPrawAdapter
from mvp_scrapping.app.adapters.storage_adapter import StorageAdapter
from unittest.mock import MagicMock
import pandas as pd

def test_full_integration(tmpdir):
    # Mock API Reddit
    reddit_mock = MagicMock()
    post_mock = MagicMock()
    reddit_mock.subreddit.return_value.top.return_value = [post_mock]

    post_mock.id = "post_id"
    post_mock.title = "Test Title"
    post_mock.author.name = "TestAuthor"
    post_mock.selftext = "Test content with http://example.com"
    post_mock.score = 100
    post_mock.num_comments = 5
    post_mock.comments.list.return_value = []

    # Configura o adaptador de Reddit com mock
    reddit_adapter = RedditPrawAdapter(client_id=os.getenv("CLIENT_ID"), client_secret=os.getenv("CLIENT_SECRET"), user_agent=os.getenv("CLIENT_AGENT"))
    reddit_adapter.reddit = reddit_mock

    # Scrape e anonimize os dados
    posts = reddit_adapter.fetch_top_posts("test_subreddit", limit=1)
    
    # Verifica se o post foi coletado e anonimizado corretamente
    assert posts[0]['Title'] == "Test Title"
    assert posts[0]['Author'] != "TestAuthor"  # Autor deve estar anonimizado
    assert posts[0]['Text'] == "Test content with [URL]"
    
    # Salva os dados em CSV temporário
    storage_adapter = StorageAdapter()
    file_path = os.path.join(tmpdir, 'test_data.csv')
    storage_adapter.save_to_json(posts, file_path)
    storage_adapter.save_to_csv(posts, file_path)
    
    # Verifica se os dados foram salvos corretamente
    df = pd.read_csv(file_path)
    assert df.iloc[0]['Title'] == "Test Title"
