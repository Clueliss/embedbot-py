from embedbot_post_recv import base
import requests
import bs4
import json


class NineGagPost(base.Post):
    def __init__(self, title: str, embed_url: str, post_type: base.PostType):
        base.Post.__init__(self, "9GAG", title, embed_url, post_type, "9GAG")

    @property
    def origin(self) -> str:
        return "9gag.com/{}".format(base.Post.origin)


class NineGagApi(base.API):
    @staticmethod
    def _find_website_build_json(html: bs4.BeautifulSoup):
        scripts = html.find_all("script", attrs={"type": "text/javascript", "src": ""})
        return json.loads(scripts[len(scripts) - 1].text[29:-3].replace("\\", ""))

    @staticmethod
    def _get_post_type(post_type_str: str) -> base.PostType:
        if post_type_str == "Photo":
            return base.PostType.Image
        else:
            return base.PostType.Video

    @staticmethod
    def _get_post_url(post_json) -> str:
        if post_json["type"] == "Photo":
            return post_json["images"]["image700"]["url"]
        elif post_json["type"] == "Animated":
            return post_json["images"]["image460svwm"]["url"]
        else:
            return post_json["vp9Url"]

    def parse_post(self, raw: requests.Response) -> base.Post:
        html = bs4.BeautifulSoup(raw.text, "html.parser")
        title = html.find("title").text

        build_json = NineGagApi._find_website_build_json(html)
        post_json = build_json["data"]["post"]

        post_type = NineGagApi._get_post_type(post_json["type"])
        embed_url = NineGagApi._get_post_url(post_json)

        return NineGagPost(title, embed_url, post_type)
