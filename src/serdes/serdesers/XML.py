import typing

import xmltodict

from serdesers.base import BaseSerDes


class XmlSerDes(BaseSerDes):
    def __init__(self):
        super().__init__()
        self.format = "XML"

    def serialize(self, data: dict[str, typing.Any]):
        return xmltodict.unparse({"data": data})

    def deserialize(self, data: bytes):
        return dict(xmltodict.parse(data))["data"]


if __name__ == '__main__':
    from tester import Tester
    import logging
    s = XmlSerDes()
    t = Tester(s)
    logging.basicConfig(level=logging.DEBUG)
    print(t.test({"a": "1", "b": ["1", "2"]}))
