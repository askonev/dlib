# -*- coding: utf-8 -*-

import pafy
from lib.ydl_client import YdlClient


url: str = ''

# Create class instance
ydl_video = YdlClient(url)
ydl_video.download()
