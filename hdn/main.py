import requests


class HDNWorker:
    def __init__(self, token, ip="127.0.0.1", port=7979):
        self.token = token
        self.ip = ip
        self.port = 7979
        self.session = requests.Session()

    def task(self, f, main=False, info=None):
        return f

    def dump(self):
        pass
