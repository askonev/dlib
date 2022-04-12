# -*- coding: utf-8 -*-

import pafy
from lib.client import Client


class YdlClient:
    """Constructor"""

    def __init__(self, url_vid):
        """Constructor"""
        self.yt_video = pafy.new(url_vid)

    def download(self):

        try:

            self.yt_video.streams[Client().user_choice(self.yt_video.streams)].download('./tmp')

        except:
            print('Error')
