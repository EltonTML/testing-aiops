# main.py
import requests
from models import Post, Base, engine, SessionLocal

def fetch_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    try:
        response = requests.get(url)
        response.raise_for_status()
        posts = response.json()
        return posts[:5]  # Only take first 5 for demo
    except requests.exceptions.RequestException as e:
        print(f"Error fetching posts: {e}")
        return []

def save_posts_to_db(posts):
    Base.metadata.create_all(bind=engine)
    with SessionLocal() as session:
        for post_data in posts:
            post = Post(id=post_data['id'], title=post_data['title'], body=post_data['body'])
            session.merge(post)  # merge to avoid duplicates on re-run
        session.commit()
    print("Posts saved to database.")

if __name__ == "__main__":
    posts = fetch_posts()
    if posts:
        save_posts_to_db(posts)
