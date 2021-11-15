from typing import Dict, List

from sequence.impls import  SequenceOne, SequenceThree, SequenceTwo
from sequence.abstract_sequence import Sequence


class FailedToCreateSequencesException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class SequenceFactory:
    def __init__(self) -> None:
        self.seq_map = {
            SequenceOne.__name__: SequenceOne,
            SequenceTwo.__name__: SequenceTwo,
            SequenceThree.__name__: SequenceThree,
        }

    def create_sequences(
        self, requested_sequences: Dict, errors: List[str]
    ) -> List[Sequence]:
        sequences = []
        for name, conf in requested_sequences.items():
            if "type" in conf:
                if conf["type"] in self.seq_map:
                    if "config" in conf:
                        try:
                            sequences.append(
                                self.seq_map[conf["type"]](name, conf["config"])
                            )
                        except Exception as e:
                            errors.append(
                                f"failed to add sequence '{name}', exception: {e}"
                            )
                    else:
                        errors.append(
                            f"requested sequence does not have 'config' defined: seq={name, conf}"
                        )
                else:
                    errors.append(
                        f"requested sequence not available: name={name, conf}, available sequences={list(self.seq_map.keys())}"
                    )
            else:
                errors.append(f"requested sequence missing 'type': seq={name, conf}")
        if errors:
            raise FailedToCreateSequencesException(errors)
        return sequences
