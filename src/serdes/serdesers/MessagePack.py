import typing

import msgpack

from serdesers.base import BaseSerDes


class MsgpackSerDes(BaseSerDes):
    def __init__(self):
        super().__init__()
        self.format = "MessagePack"

    def serialize(self, data: dict[str, typing.Any]):
        return msgpack.packb(data)

    def deserialize(self, data: bytes):
        return msgpack.unpackb(data)


if __name__ == '__main__':
    from tester import Tester
    import logging
    s = MsgpackSerDes()
    t = Tester(s)
    logging.basicConfig(level=logging.DEBUG)
    print(t.test({"1": 1, "2": "2"}))
