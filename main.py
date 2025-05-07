# main.py
import requests
from models import Post, Base, engine, SessionLocal

def fetch_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()[:5]  # Only first 5 posts
    except requests.exceptions.RequestException as e:
        print(f"Error fetching posts: {e}")
        return []

def save_posts_to_db(posts):
    Base.metadata.create_all(bind=engine)
    session = SessionLocal()
    try:
        for post_data in posts:
            post = Post(id=post_data['id'], title=post_data['title'], body=post_data['body'])
            session.merge(post)  # merge avoids duplicates on re-run
        session.commit()
        print("Posts saved to SQLite database.")
    except Exception as e:
        session.rollback()
        print(f"Error saving posts to database: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    posts = fetch_posts()
    if posts:
        save_posts_to_db(posts)
