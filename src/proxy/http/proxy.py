import os
from flask import Flask, request
import requests

FORMATS = ["native", "xml", "json", "protobuf", "avro", "yaml", "msgpack"]

app = Flask(__name__)


@app.route('/get_result')
def get_result():
    format = request.args.get("format")
    if not format:
        format = "native"

    if format == "all":
        result = {}
        for format in FORMATS:
            result[format] = requests.get(f"http://{format}:{SERDES_HTTP_PORT}/get_result").text
        return result

    return requests.get(f"http://{format}:{SERDES_HTTP_PORT}/get_result").text


if __name__ == '__main__':
    HTTP_IP = os.getenv("HTTP_IP", default="0.0.0.0")
    HTTP_PORT = os.getenv("HTTP_PORT", default=2000)

    SERDES_HTTP_PORT = os.getenv("SERDES_HTTP_PORT", default=5000)
    app.run(HTTP_IP, port=HTTP_PORT)
