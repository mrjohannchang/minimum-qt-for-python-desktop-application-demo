import argparse

import sdk_demo as sdk
import dacite


def edit(args: argparse.Namespace):
    datum: sdk.Datum = dacite.from_dict(data_class=sdk.Datum, data=args.__dict__)
    sdk.edit_datum(database_path=args.database, datum=datum)
