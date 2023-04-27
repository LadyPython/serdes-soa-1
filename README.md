# Instructions
### UDP version
```commandline
docker compose pull
docker compose up
echo "get_result all" | nc -u localhost 2000
```


### HTTP version
```commandline
docker compose pull
docker compose -f docker-compose-http.yml up
curl -X GET "http://localhost:2000/get_result?format=all"
```

# Testing data structure
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

# Implementation option
Очень продвинутый

## Proxy
[/src/proxy](/src/proxy)


# Data formats
All:
1. Native (pickle)
2. XML 
3. JSON 
4. Google Protocol Buffers 
5. Apache Avro 
6. YAML 
7. MessagePack

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
