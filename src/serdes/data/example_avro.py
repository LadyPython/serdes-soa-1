from dataclasses import dataclass, field

from dataclasses_avroschema import AvroModel


@dataclass
class EmptyExample(AvroModel):
    string: str = ""
    array: list[int] = field(default_factory=list)
    dictionary: dict[str, str] = field(default_factory=dict)
    integer: int = 0
    double: float = 0.0
    boolean: bool = False


@dataclass
class Example(AvroModel):
    string: str
    array: list[int]
    dictionary: dict[str, str]
    integer: int
    double: float
    boolean: bool
    empty_subclass: EmptyExample = field(default_factory=EmptyExample)
