import importlib
from sequence import Sequence

from sequence_factory import SequenceFactory

sf = SequenceFactory()


def importlib_creation():
    ilso_cls = getattr(importlib.import_module("seq_one"), "SequenceOne")
    ilso = ilso_cls("MyName", {"value": "importlib"})
    print(ilso.name, ilso.config)


def clean_factory_creation():
    errors = []
    conf = {
        "Foo": {
            "type": "SequenceOne",
            "config": {
                "value": "myval",
            },
        },
        "Bar": {
            "type": "SequenceOne",
            "config": {
                "value": "secondval",
            },
        },
        "Zip": {
            "type": "SequenceTwo",
            "config": {
                "value": "seqtwoval",
            },
        },
    }

    ss = sf.get_sequences(conf, errors)
    print(ss)
    for s in ss:
        print(type(s))
        print(isinstance(s, Sequence))
        print(s.name, s.config)
        s.sequence()
    print(errors)
    print(Sequence.__subclasses__())


def bad_factory_creation():
    errors = []
    bad_conf = {
        "Foo": {
            "type": "SequenceOne",
            "config": {
                "value": "myval",
            },
        },
        "Bar": {
            "type": "SequenceOne",
            "config": {
                "value": "secondval",
            },
        },
        "Baz": {
            "type": "SequenceOne",
        },
        "Boop": {
            "type": "SequenceOne",
            "config": {},
        },
        "Zip": {
            "type": "SequenceTwo",
        },
        "Wiz": {
            "config": {
                "value": "no type specified",
            }
        },
        "Bang": {
            "type": "NotThere",
        },
    }
    try:
        ss = sf.get_sequences(bad_conf, errors)
        print(ss)
        for s in ss:
            print(s.name, s.config)
        print(errors)
    except Exception as e:
        print(e)


def sequence_three_not_instantiable():
    seq_dict = {
        "Three": {
            "type": "SequenceThree",
            "config": {},
        }
    }
    errors = []
    ss = sf.get_sequences(seq_dict, errors)
    for s in ss:
        print(s)


def main():
    importlib_creation()
    clean_factory_creation()
    bad_factory_creation()
    sequence_three_not_instantiable()


if __name__ == "__main__":
    main()
