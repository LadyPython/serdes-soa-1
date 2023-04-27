import pickle

from serdesers.base import BaseSerDes


class NativeSerDes(BaseSerDes):
    def __init__(self):
        super().__init__()
        self.format = "native (pickle)"

    def serialize(self, data):
        return pickle.dumps(data)

    def deserialize(self, data: bytes):
        return pickle.loads(data)


if __name__ == '__main__':
    from tester import Tester
    import logging
    s = NativeSerDes()
    t = Tester(s)
    logging.basicConfig(level=logging.DEBUG)
    print(t.test({"1": 1, 2: "2"}))
