from enum import Enum
import requests


class PostType(Enum):
    Image = 0
    Video = 1


class Post:
    def __init__(self, website: str, title: str, embed_url: str, post_type: PostType, origin: str):
        self._website = website
        self._title = title
        self._embed_url = embed_url
        self._post_type = post_type
        self._origin = origin

    @property
    def website(self) -> str:
        return self._website

    @property
    def post_type(self) -> PostType:
        return self._post_type

    @property
    def title(self) -> str:
        return self._title

    @property
    def embed_url(self) -> str:
        return self._embed_url

    @property
    def origin(self) -> str:
        return self._origin


class API:
    def __init__(self, **kwargs):
        pass

    def wget(self, url: str) -> requests.Response:
        return requests.get(url)

    def parse_post(self, raw: requests.Response) -> Post:
        raise NotImplementedError()

    def get_post(self, url: str) -> Post:
        res = self.wget(url)
        return self.parse_post(res)


