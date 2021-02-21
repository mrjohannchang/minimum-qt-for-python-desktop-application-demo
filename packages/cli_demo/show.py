import argparse
import dataclasses
import json

import sdk_demo as sdk


def show(args: argparse.Namespace):
    if not args.record_nos:
        print(json.dumps(list(sdk.get_record_nos(database_path=args.database)), indent=args.indent))
    elif len(args.record_nos) == 1:
        print(json.dumps(dataclasses.asdict(
            sdk.get_datum(database_path=args.database, record_no=args.record_nos[0])), indent=args.indent))
    else:
        datum: sdk.Datum
        for datum in sdk.get_data(database_path=args.database, record_nos=args.record_nos):
            print(json.dumps(dataclasses.asdict(datum), indent=args.indent))
