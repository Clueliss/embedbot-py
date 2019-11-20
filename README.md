# Embedbot [DEPRECATED]

## Introduction

> This is a discord bot that will embed
- 9GAG videos 
- reddit images
> It will not embed
- 9GAG images (since discord embeds them just fine)
- reddit videos (since i have yet to figure out how to embed .m3u8 files)

## Problems
> This project is under active development (whenever i am bored) and may have bugs, they should mostly appear when embedding from 9GAG since 9GAG does not provide a public API to view post metadata. This bot basically parses JSON inside a javascript script on the posts page, which is not optimal but the best solution i have found yet.

## Dependencies
- systemd (optional if you want to run the bot via the provided service file)
- python3
> and the following python packages
- bs4 (BeautifulSoup)
- discord
- json
- requests

## Installation
> \# python3 -m pip install bs4 discord json requests  
> \# sh ./install.sh

## Configuration
> put your discord access token into /etc/embedbot.conf
