from typing import Dict

from sequence import InvalidConfig, Sequence


class SequenceOne(Sequence):
    def __init__(self, name: str, config: Dict) -> None:
        super().__init__(name, config)

    def sequence(self) -> None:
        return super().sequence()

    def validate_config(self, config) -> Dict:
        errors = []
        if "value" not in config:
            errors.append(f"'value' must be set in config, {config}; name={self.name}")

        if errors:
            raise InvalidConfig(errors)
        return config
