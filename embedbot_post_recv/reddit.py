import requests
from embedbot_post_recv import base


class RedditPost(base.Post):
    def __init__(self, title: str, embed_url: str, post_type: base.PostType, origin: str):
        base.Post.__init__(self, "reddit", title, embed_url, post_type, origin)

class RedditAPI(base.API):
    def parse_post(self, raw: requests.Response) -> RedditPost:
        apijson = raw.json()

        post_data = apijson[0]["data"]["children"][0]["data"]

        title = post_data["title"]
        url = post_data["url"]
        is_video = base.PostType.Video if post_data["is_video"] else base.PostType.Image
        subreddit = post_data["subreddit"]

        return RedditPost(title, url, is_video, "reddit.com/r/{}".format(subreddit))

    def get_post(self, url: str) -> RedditPost:
        resp = requests.get("{}/.json".format(url), headers={"User-agent": "embedbot v0.1"})
        return self.parse_post(resp)
