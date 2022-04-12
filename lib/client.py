# -*- coding: utf-8 -*-

class Client:
    """ Class for interactions """

    @staticmethod
    def user_choice(plist):
        """
        Asks the user which sheet item he chooses

        @param [string] plist
        """

        count = 0
        for stream in plist:
            print(f"{count}: {stream}")
            count += 1

        response = int(input('Enter number of current assurance: '))
        return response
