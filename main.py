# main.py
import requests

def fetch_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    try:
        response = requests.get(url)
        response.raise_for_status()
        posts = response.json()
        for post in posts[:5]:
            print(f"Post ID: {post['id1']}")
            print(f"Title: {post['title1']}")
            print(f"Body: {post['body1']}\n")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching posts: {e}")

if __name__ == "__main__":
    fetch_posts()
