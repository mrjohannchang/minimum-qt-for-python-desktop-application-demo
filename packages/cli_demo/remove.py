import argparse

import dacite
import sdk_demo as sdk


def remove(args: argparse.Namespace) -> None:
    datum: sdk.Datum = dacite.from_dict(data_class=sdk.Datum, data=args.__dict__)
    sdk.remove_datum(database_path=args.database, id=datum.id)
