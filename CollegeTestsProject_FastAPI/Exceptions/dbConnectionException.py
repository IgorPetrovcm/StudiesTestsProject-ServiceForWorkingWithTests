class DbConnectionException(Exception):
    def __init__(self, *args: object):
        if args[0] != None:
            self.__message = args[0]
        else:
            self.__message = None

    @property
    def message(self):
        return self.__message