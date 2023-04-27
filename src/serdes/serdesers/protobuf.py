from serdesers.base import BaseSerDes


class ProtobufSerDes(BaseSerDes):
    def __init__(self, schema):
        super().__init__()
        self.format = "Google Protocol Buffers"
        self.schema = schema

    def serialize(self, data):
        return data.SerializeToString()

    def deserialize(self, data: bytes):
        self.schema.ParseFromString(data)
        return self.schema


if __name__ == '__main__':
    from tester import Tester
    import logging
    from data.example_pb2 import Example, EmptyExample

    s = ProtobufSerDes(Example())
    t = Tester(s)
    logging.basicConfig(level=logging.DEBUG)

    example = Example()
    example.string = "Sofia Semenova-Zvenigorodskaya"
    example.array.extend([1, -2, 3, -4, 100500, -500100])
    example.dictionary["cat"] = "mew"
    example.dictionary["dog"] = "bark"
    example.integer = 123456789000
    example.double = -3.14159265359
    example.boolean = True
    example.empty_subclass.CopyFrom(EmptyExample())
    print(t.test(example))
