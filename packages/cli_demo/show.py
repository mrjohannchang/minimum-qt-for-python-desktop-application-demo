import argparse
import dataclasses
import json

import sdk_demo as sdk


def show(args: argparse.Namespace) -> None:
    if not args.ids:
        print(json.dumps(list(sdk.get_ids(database_path=args.database)), indent=args.indent))
    elif len(args.ids) == 1:
        print(json.dumps(dataclasses.asdict(
            sdk.get_datum(database_path=args.database, id=args.ids[0])), indent=args.indent))
    else:
        datum: sdk.Datum
        for datum in sdk.get_data(database_path=args.database, ids=args.ids):
            print(json.dumps(dataclasses.asdict(datum), indent=args.indent))
