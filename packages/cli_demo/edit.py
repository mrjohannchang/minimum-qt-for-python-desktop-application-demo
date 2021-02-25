import argparse

import dacite
import sdk_demo as sdk


def edit(args: argparse.Namespace) -> None:
    datum: sdk.Datum = dacite.from_dict(data_class=sdk.Datum, data=args.__dict__)
    sdk.edit_datum(database_path=args.database, datum=datum)
