replies = {}

class Response:

    def __init__(self, data):
        self.data = data

    def json(self):
        return self.data

def get(url):

    return Response(replies[url])