import importlib

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
        print(s.name, s.config)
        s.sequence()
    print(errors)


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
    ss = sf.get_sequences(bad_conf, errors)
    print(ss)
    for s in ss:
        print(s.name, s.config)
    print(errors)


def main():
    importlib_creation()
    clean_factory_creation()
    bad_factory_creation()


if __name__ == "__main__":
    main()
