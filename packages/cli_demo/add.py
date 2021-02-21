import argparse

import sdk_demo as sdk
import dacite


def add(args: argparse.Namespace):
    datum: sdk.Datum = dacite.from_dict(data_class=sdk.Datum, data=args.__dict__)
    sdk.add_datum(database_path=args.database, datum=datum)
