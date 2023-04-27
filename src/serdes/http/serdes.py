import os
from flask import Flask

from serdesers.JSON import JsonSerDes
from serdesers.MessagePack import MsgpackSerDes
from serdesers.XML import XmlSerDes
from serdesers.YAML import YamlSerDes
from serdesers.avro import AvroSerDes
import data.example_avro as avro_example
from serdesers.base import BaseSerDes
from data.example import Example
from serdesers.native import NativeSerDes
from serdesers.protobuf import ProtobufSerDes
import data.example_pb2 as example_pb2

from tester import Tester


def get_serdes(format: str) -> BaseSerDes:
    match format:
        case "native":
            return NativeSerDes()
        case "xml":
            return XmlSerDes()
        case "json":
            return JsonSerDes()
        case "protobuf":
            return ProtobufSerDes(example_pb2.Example())
        case "avro":
            return AvroSerDes(avro_example.Example)
        case "yaml":
            return YamlSerDes()
        case "msgpack":
            return MsgpackSerDes()

        case _:
            raise Exception(f"Unknown format {format}")


def get_data(format: str) -> Example | dict | avro_example.Example | example_pb2.Example:
    match format:
        case ("xml" | "msgpack"):
            return {
                "string": "Sofia Semenova-Zvenigorodskaya @LadyPython!",
                "array": [1, -2, 3, -4, 100500, -500000000],
                "dictionary": {"cat": "mew", "dog": "bark"},
                "integer": 123456789000,
                "double": -3.14159265359,
                "boolean": True,
                "empty_subclass": {
                    "string": "",
                    "array": [],
                    "dictionary": {},
                    "integer": 0,
                    "double": 0.0,
                    "boolean": False,
                }
            }
        case "protobuf":
            example = example_pb2.Example()
            example.string = "Sofia Semenova-Zvenigorodskaya @LadyPython!"
            example.array.extend([1, -2, 3, -4, 100500, -500000000])
            example.dictionary["cat"] = "mew"
            example.dictionary["dog"] = "bark"
            example.integer = 123456789000
            example.double = -3.14159265359
            example.boolean = True
            example.empty_subclass.CopyFrom(example_pb2.EmptyExample())
            return example
        case "avro":
            return avro_example.Example(
                string="Sofia Semenova-Zvenigorodskaya @LadyPython!",
                array=[1, -2, 3, -4, 100500, -500000000],
                dictionary={"cat": "mew", "dog": "bark"},
                integer=123456789000,
                double=-3.14159265359,
                boolean=True
            )
        case _:
            return Example(
                string="Sofia Semenova-Zvenigorodskaya @LadyPython!",
                array=[1, -2, 3, -4, 100500, -500000000],
                dictionary={"cat": "mew", "dog": "bark"},
                integer=123456789000,
                double=-3.14159265359,
                boolean=True
            )


app = Flask(__name__)


@app.route('/get_result')
def get_result():
    tester = Tester(get_serdes(FORMAT))
    return str(tester.test(get_data(FORMAT)))


if __name__ == '__main__':
    FORMAT = os.getenv("SERDES_FORMAT", default="native")
    HTTP_IP = os.getenv("HTTP_IP", default="0.0.0.0")
    HTTP_PORT = os.getenv("HTTP_PORT", default=5000)

    app.run(HTTP_IP, port=HTTP_PORT)
