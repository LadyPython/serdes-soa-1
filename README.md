# Instructions
## Setup
```commandline
docker compose up
```

In order to switch from UDP to the HTTP version, you will need to include the `-f` option.
```commandline
docker compose -f docker-compose-http.yml up
```

## Requests
### Supported data serialization formats
1. Native (pickle) `native`
2. XML `xml`
3. JSON `json`
4. Google Protocol Buffers `protobuf`
5. Apache Avro `avro`
6. YAML `yaml`
7. MessagePack `msgpack`

```commandline
echo "get_result [format_name]" | nc -u localhost 2000
```
```commandline
curl -X GET "http://localhost:2000/get_result?format=[format_name]"
```

Response representation: `format - serialized size - serialization time (ms) - deserialization time (ms)`

If you want to retrieve information about all formats simultaneously, you can use `all` for the `format_name` parameter.

## Testing data structure
```python
Example(
    string="Sofia Semenova-Zvenigorodskaya @LadyPython!",
    array=[1, -2, 3, -4, 100500, -500000000],
    dictionary={"cat": "mew", "dog": "bark"},
    integer=123456789000,
    double=-3.14159265359,
    boolean=True,
    empty_subclass=EmptyExample(
        string="",
        array=[],
        dictionary={},
        integer=0,
        double=0.0,
        boolean=False
    )
)
```

## Examples
```commandline
echo "get_result json" | nc -u localhost 2000

json - 406 - 84ms - 76ms
```

```commandline
echo "get_result all" | nc -u localhost 2000

Google Protocol Buffers - 127 - 1ms - 1ms
MessagePack - 222 - 5ms - 3ms
native (pickle) - 301 - 8ms - 8ms
json - 406 - 84ms - 90ms
XML - 502 - 92ms - 93ms
Apache Avro - 105 - 1050ms - 1763ms
YAML - 374 - 790ms - 2203ms
```

```commandline
curl -X GET "http://localhost:2000/get_result?format=native"

native (pickle) - 301 - 8ms - 8ms
```

```commandline
curl -X GET "http://localhost:2000/get_result?format=all"

{
    "avro": "Apache Avro - 105 - 834ms - 860ms",
    "json": "json - 406 - 71ms - 76ms",
    "msgpack": "MessagePack - 222 - 2ms - 3ms",
    "native": "native (pickle) - 301 - 8ms - 9ms",
    "protobuf": "Google Protocol Buffers - 127 - 1ms - 1ms",
    "xml": "XML - 502 - 93ms - 83ms",
    "yaml": "YAML - 374 - 904ms - 1542ms"
}
```

# Implementation details
Очень продвинутый 🐍💪

## UDP version
[/src/proxy/udp](/src/proxy/udp)

[/src/serdes/udp](/src/serdes/udp)

The default proxy address is listening at `0.0.0.0:2000`, and the default multicast group address is `224.1.1.1`. 
You have the option to modify these settings by using the `UDP_IP`, `UDP_PORT`, and `MCAST_GRP` environment variables.

Similarly, the serializers are also set to their default address at `0.0.0.0:2000`, and you can customize their 
location using the `UDP_IP` and `UDP_PORT` variables. If you decide to change the `UDP_PORT` for the serializers, 
you must also update the `SERDES_UDP_PORT` for the proxy with the same value.

## HTTP version
[/src/proxy/http](/src/proxy/http)

[/src/serdes/http](/src/serdes/http)

By default, the proxy address is `0.0.0.0:2000`, and the serializer addresses are `0.0.0.0:5000`. 
You can change these addresses using the `HTTP_IP`, `HTTP_PORT`, and `SERDES_HTTP_PORT` environment variables.

# Results

| Format   | Serialized data size (bytes) | Serialization time (ms) | Deserialization time (ms) |
|----------|------------------------------|-------------------------|---------------------------|
| native   | 301                          | 9                       | 9                         |
| xml      | 502                          | 101                     | 88                        |
| json     | 406                          | 94                      | 84                        |
| protobuf | 127                          | 1                       | 1                         |
| avro     | 105                          | 856                     | 861                       |
| yaml     | 374                          | 774                     | 1337                      |
| msgpack  | 222                          | 2                       | 3                         |
