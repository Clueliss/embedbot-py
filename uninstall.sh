#!/bin/sh

systemctl disable embedbot.service --now                        # stop and disable service
rm /usr/bin/embedbot.py                                         # exec
rm /etc/systemd/system/embedbot.service                         # service
rm -r /usr/local/lib/python3.7/site-packages/embedbot_post_recv # libs

read -p "Do you also want to delete /etc/embedbot.conf? remember: it contains your bot token (y/n)" choice

case "$choice" in 
  y|Y ) rm /etc/embedbot.conf;;                                 # config
  n|N ) ;;
  * ) echo "invalid";;
esac
