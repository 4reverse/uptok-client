# uptok

Python client for uptok API (http://api.uptok.ru/docs)

## Installation

### Install from GitHub

```bash
pip install git+https://github.com/4reverse/uptok.git
```

### Install for development

```bash
git clone https://github.com/4reverse/uptok.git
cd uptok
pip install -e .
```

## Example usage

```python
from uptok import UPTok

# Initialize client
client = UPTok(key="your_api_key")

# Get user ID by username
user_id = client.get_user_id("username")

# Get user information
user_info = client.get_user("user_id")

# Get user followers
followers = client.get_user_followers("user_id", count=20, offset=0, page_token="")

# Search users
users = client.search_user_by_keyword("keyword", count=10, offset=0)

# Search videos
videos = client.search_video_by_keyword("keyword", count=10, offset=0)
```

More API docs: https://api.uptok.ru/docs

## License

MIT
