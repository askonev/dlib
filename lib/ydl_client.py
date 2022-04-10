# -*- coding: utf-8 -*-

import pafy


class YdlClient:
    """Constructor"""

    def __init__(self, url_vid):
        """Constructor"""
        self.obj_video = pafy.new(url_vid)
        self.streams = self.obj_video.streams

    def download(self):

        try:
            print(self.streams)
        #     streams = v.streams  # video with audio
        #     print(streams)
        #
        #     availiable_streams = {}
        #     count = 0
        #
        #     for stream in streams:
        #         availiable_streams[count] = stream
        #         print(f"{count}: {stream}")
        #         count += 1
        #
        #     stream_count = int(input('Enter number of current assurance: '))
        #     d = streams[stream_count].download(filepath="./tmp")
        #
        #     print('Download successfully')

        except:
            print('Some error')
