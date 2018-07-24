class BadValue(Exception):

    def __init__(self, message):
        super(BadValue, self).__init__(message)