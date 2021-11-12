from typing import Dict
from sequence import Sequence


class SequenceThree(Sequence):
    def __init__(self, name: str, config: Dict) -> None:
        super().__init__(name, config)

    