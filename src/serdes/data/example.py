from dataclasses import dataclass, field


@dataclass
class EmptyExample:
    string: str = ""
    array: list[int] = field(default_factory=list)
    dictionary: dict[str, str] = field(default_factory=dict)
    integer: int = 0
    double: float = 0.0
    boolean: bool = False


@dataclass
class Example:
    string: str
    array: list[int]
    dictionary: dict[str, str]
    integer: int
    double: float
    boolean: bool
    empty_subclass: EmptyExample = field(default_factory=EmptyExample)
