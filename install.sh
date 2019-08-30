#!/bin/sh

cp ./embedbot.py /usr/bin                                          # exec
touch /etc/embedbot.conf                                           # config
cp ./embedbot.service /etc/systemd/system                          # service
cp -r ./embedbot_post_recv /usr/local/lib/python3.7/site-packages/ # libraries
