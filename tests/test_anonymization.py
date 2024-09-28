import os

import hashlib
from mvp_scrapping.app.adapters.reddit_praw_adapter import RedditPrawAdapter


def test_anonymize_author():
    adapter = RedditPrawAdapter(client_id=os.getenv("CLIENT_ID"), client_secret=os.getenv("CLIENT_SECRET"), user_agent=os.getenv("CLIENT_AGENT"))
    
    # Testa anonimização de nome
    author_name = "JohnDoe"
    anon_author = adapter.anonymize_author(author_name)
    
    expected_hash = hashlib.sha256(author_name.encode()).hexdigest()
    assert anon_author == expected_hash
    
    # Testa anonimização de autor nulo
    assert adapter.anonymize_author(None) == "Anônimo"

def test_anonymize_text():
    adapter = RedditPrawAdapter("client_id", "client_secret", "user_agent")
    
    text_with_url = "Check this out: http://example.com"
    anon_text = adapter.anonymize_text(text_with_url)
    
    assert anon_text == "Check this out: [URL]"
