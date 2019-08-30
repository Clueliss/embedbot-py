#!/usr/bin/env python3

import discord
import platform
import typing

from embedbot_post_recv import base, ninegag, reddit

if platform.system() == "Windows":
    BIN_DIR = ""
    CONF_DIR = ""
else:
    BIN_DIR = "/usr/bin/"
    CONF_DIR = "/etc/"


def is_url(url: str) -> bool:
    return url.startswith("https://") or url.startswith("http://")


def is_9gag_url(url: str) -> bool:
    return url.startswith("https://9gag.com")


def is_reddit_url(url: str) -> bool:
    return url.startswith("https://www.reddit.com")


def should_embed(post: base.Post) -> bool:
    return (post.website.lower() == "reddit" and post.post_type == base.PostType.Image) \
           or (post.website.lower() == "9gag" and post.post_type == base.PostType.Video)


class GIFExpandClient(discord.Client):

    @staticmethod
    def _escape_title(title: str) -> str:
        return title.replace("*", "\\*") \
            .replace("_", "\\_") \
            .replace("~", "\\~")

    @staticmethod
    def _get_appropriate_api(url: str) -> typing.Union[base.API, None]:
        if is_reddit_url(url):
            return reddit.RedditAPI()
        elif is_9gag_url(url):
            return ninegag.NineGagApi()
        else:
            return None

    async def on_ready(self):
        print("<6> Logged in")

    async def on_message(self, msg: discord.Message):

        api = GIFExpandClient._get_appropriate_api(msg.content)

        if api is None:
            if is_url(msg.content):
                print("<5> could not get embedbot_post_recv for '{}'".format(msg.content))
            return

        post = api.get_post(msg.content)

        if should_embed(post):
            title = GIFExpandClient._escape_title(post.title)

            if post.post_type == base.PostType.Image:
                embed = discord.Embed(title='"{}"'.format(title), url=msg.content, description=post.origin)
                embed.set_author(name=msg.author)
                embed.set_image(url=post.embed_url)

                await msg.channel.send(embed=embed)

                print("<7> embedded {} image".format(post.website))
            else:
                await msg.channel.send('>>> Sender: **{}**\nSource: <{}>\nEmbedURL: {}\n\n**"{}"**'
                                       .format(msg.author, msg.content, post.embed_url, title))

                print("<7> embedded {} video".format(post.website))

            await msg.delete()
        else:
            print("<7> ignored '{}'".format(msg.content))
            

with open("{}embedbot.conf".format(CONF_DIR), "r") as tok_file:
    tok = tok_file.readline().strip()


client = GIFExpandClient()
client.run(tok)
