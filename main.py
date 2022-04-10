# -*- coding: utf-8 -*-

from lib.ydl_client import YdlClient
# from lib.interacting
import pafy

url: str = 'https://youtu.be/adeiXxweK6g'
# print(url_video)

obj_video = YdlClient(url)

obj_video.download()
