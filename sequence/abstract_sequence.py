from abc import ABC, abstractmethod
from typing import Dict


class InvalidConfig(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class Sequence(ABC):
    def __init__(self, name: str, config: Dict) -> None:
        self.name = name
        self.config = self.validate_config(config)

    @abstractmethod
    def sequence(self) -> None:
        print(self.config["value"])

    @abstractmethod
    def validate_config(self, config) -> Dict:
        return config
