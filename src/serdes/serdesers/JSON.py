import jsonpickle

from serdesers.base import BaseSerDes


class JsonSerDes(BaseSerDes):
    def __init__(self):
        super().__init__()
        self.format = "json"

    def serialize(self, data):
        return jsonpickle.encode(data)

    def deserialize(self, data: bytes):
        return jsonpickle.decode(data)


if __name__ == '__main__':
    from tester import Tester
    import logging
    s = JsonSerDes()
    t = Tester(s)
    logging.basicConfig(level=logging.DEBUG)
    print(t.test({"1": 1, "2": "2"}))
