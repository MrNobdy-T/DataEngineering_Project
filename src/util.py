import requests
from datetime import datetime
class RedditDeepScraper:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) ResearchBot/2.0"})

    def fetch_all_comments(self, subreddit, post_id):
        url = f"https://www.reddit.com/r/{subreddit}/comments/{post_id}.json"
        response = self.session.get(url)
        if response.status_code != 200:
            return []

        # Reddit JSON structure: [PostObject, CommentObject]
        # We target the 'children' in the CommentObject
        comment_forest = response.json()[1]['data']['children']

        flat_comments = []
        self._parse_tree(comment_forest, flat_comments)
        return flat_comments

    def _parse_tree(self, children, result_list):
        """Recursively walks the comment tree to flatten it."""
        for child in children:
            if child['kind'] == 't1':  # t1 = Comment
                data = child['data']
                result_list.append({
                    "comment_id": data.get('id'),
                    "parent_id": data.get('parent_id'),
                    "author": data.get('author'),
                    "body": data.get('body'),
                    "score": data.get('score'),
                    "created_utc": datetime.fromtimestamp(data.get('created_utc')) if data.get('created_utc') else None
                })

                # Check for replies (nested tree)
                replies = data.get('replies')
                if replies and isinstance(replies, dict):
                    inner_children = replies.get('data', {}).get('children', [])
                    self._parse_tree(inner_children, result_list)