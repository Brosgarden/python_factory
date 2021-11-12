from typing import Dict

from sequence import Sequence


class SequenceTwo(Sequence):
    def __init__(self, name: str, config: Dict) -> None:
        super().__init__(name, config)

    def sequence(self) -> None:
        return super().sequence()

    def validate_config(self, config) -> Dict:
        return super().validate_config(config)
