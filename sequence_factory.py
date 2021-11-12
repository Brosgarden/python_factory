from typing import Dict, List

from sequence import Sequence


class FailedToCreateSequencesException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class SequenceFactory:
    def __init__(self) -> None:
        sequence_subclasses = Sequence.__subclasses__()
        seq_map = {}
        for sub in sequence_subclasses:
            seq_map[sub.__name__] = sub
        self.seq_map = seq_map

    def get_sequences(
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
                            f"requested_sequence does not have 'config' defined: seq={name, conf}"
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
