import yaml

from serdesers.base import BaseSerDes


class YamlSerDes(BaseSerDes):
    def __init__(self):
        super().__init__()
        self.format = "YAML"

    def serialize(self, data):
        return yaml.dump(data)

    def deserialize(self, data: bytes):
        return yaml.load(data, Loader=yaml.Loader)


if __name__ == '__main__':
    from tester import Tester
    import logging
    s = YamlSerDes()
    t = Tester(s)
    logging.basicConfig(level=logging.DEBUG)
    print(t.test({"1": 1, 2: "2"}))
