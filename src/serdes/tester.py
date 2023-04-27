import timeit
import logging
from dataclasses import dataclass

from serdesers.base import BaseSerDes


@dataclass
class TestResult:
    serializer_format: str
    serialization_time: float  # sec
    deserialization_time: float  # sec
    serialized_size: int  # bytes

    def __str__(self):
        return f"{self.serializer_format} - {self.serialized_size} - {round(self.serialization_time * 1000)}ms - {round(self.deserialization_time * 1000)}ms"


@dataclass
class Tester:
    serdes: BaseSerDes

    def test(self, data, num_runs: int = 1000) -> TestResult:
        logging.debug(f"{data=}")

        serialization_time = timeit.timeit(lambda: self.serdes.serialize(data), number=num_runs)

        serialized_data = self.serdes.serialize(data)
        logging.debug(f"{serialized_data=}")

        deserialization_time = timeit.timeit(lambda: self.serdes.deserialize(serialized_data), number=num_runs)

        deserialized_data = self.serdes.deserialize(serialized_data)
        logging.debug(f"{deserialized_data=}")

        return TestResult(self.serdes.format, serialization_time, deserialization_time, len(serialized_data))
