import typing

from dataclasses_avroschema import AvroModel

from serdesers.base import BaseSerDes


class AvroSerDes(BaseSerDes):
    def __init__(self, schema: typing.Type[AvroModel]):
        super().__init__()
        self.format = "Apache Avro"
        self.schema = schema

    def serialize(self, data: AvroModel):
        return data.serialize()

    def deserialize(self, data: bytes):
        return self.schema.deserialize(data)


if __name__ == '__main__':
    from tester import Tester
    import logging
    from data.example_avro import Example

    example = Example(
        string="Sofia Semenova-Zvenigorodskaya @LadyPython!",
        array=[1, -2, 3, -4, 100500, -500000000],
        dictionary={"cat": "mew", "dog": "bark"},
        integer=123456789000,
        double=-3.14159265359,
        boolean=True
    )

    s = AvroSerDes(Example)
    t = Tester(s)
    logging.basicConfig(level=logging.DEBUG)
    print(t.test(example))
