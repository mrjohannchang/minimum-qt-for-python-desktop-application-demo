import argparse
import os
import sys

import dataset

from .add import add
from .edit import edit
from .remove import remove
from .show import show


def parse_args() -> argparse.Namespace:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        prog="cli-demo", description="A demo of CLI application with database")
    parser.add_argument("--database", default='default.db')

    subparsers: argparse._SubParsersAction = parser.add_subparsers()

    subparser_add: argparse.ArgumentParser = subparsers.add_parser("add", help="add a record to the database")
    subparser_add.add_argument("--lab-no", required=True)
    subparser_add.add_argument("--wbc", required=True)
    subparser_add.add_argument("--rbc", required=True)
    subparser_add.add_argument("--hb", required=True)
    subparser_add.add_argument("--hct", required=True)
    subparser_add.add_argument("--mcv", required=True)
    subparser_add.add_argument("--mch", required=True)
    subparser_add.add_argument("--mchc", required=True)
    subparser_add.add_argument("--rdw-cv", required=True)
    subparser_add.add_argument("--plt", required=True)
    subparser_add.add_argument("--abn-mono", required=True)
    subparser_add.add_argument("--promonocyte", required=True)
    subparser_add.add_argument("--abn-lym", required=True)
    subparser_add.add_argument("--plasma-cell", required=True)
    subparser_add.add_argument("--blast", required=True)
    subparser_add.add_argument("--promyelocyte", required=True)
    subparser_add.add_argument("--myeloctye", required=True)
    subparser_add.add_argument("--meta-myelocyte", required=True)
    subparser_add.add_argument("--band", required=True)
    subparser_add.add_argument("--segment", required=True)
    subparser_add.add_argument("--eosinophil", required=True)
    subparser_add.add_argument("--basophil", required=True)
    subparser_add.add_argument("--lymphocyte", required=True)
    subparser_add.add_argument("--a-lym", required=True)
    subparser_add.add_argument("--monocyte", required=True)
    subparser_add.add_argument("--megakaryocyte", required=True)
    subparser_add.add_argument("--nrbc", required=True)
    subparser_add.add_argument('record_no', metavar="record_no", type=int)
    subparser_add.set_defaults(func=add)

    subparser_edit: argparse.ArgumentParser = subparsers.add_parser("edit", help="edit a record in the database")
    subparser_edit.add_argument("--lab-no")
    subparser_edit.add_argument("--wbc")
    subparser_edit.add_argument("--rbc")
    subparser_edit.add_argument("--hb")
    subparser_edit.add_argument("--hct")
    subparser_edit.add_argument("--mcv")
    subparser_edit.add_argument("--mch")
    subparser_edit.add_argument("--mchc")
    subparser_edit.add_argument("--rdw-cv")
    subparser_edit.add_argument("--plt")
    subparser_edit.add_argument("--abn-mono")
    subparser_edit.add_argument("--promonocyte")
    subparser_edit.add_argument("--abn-lym")
    subparser_edit.add_argument("--plasma-cell")
    subparser_edit.add_argument("--blast")
    subparser_edit.add_argument("--promyelocyte")
    subparser_edit.add_argument("--myeloctye")
    subparser_edit.add_argument("--meta-myelocyte")
    subparser_edit.add_argument("--band")
    subparser_edit.add_argument("--segment")
    subparser_edit.add_argument("--eosinophil")
    subparser_edit.add_argument("--basophil")
    subparser_edit.add_argument("--lymphocyte")
    subparser_edit.add_argument("--a-lym")
    subparser_edit.add_argument("--monocyte")
    subparser_edit.add_argument("--megakaryocyte")
    subparser_edit.add_argument("--nrbc", required=True)
    subparser_edit.add_argument('record_no', metavar="record-no", type=int)
    subparser_edit.set_defaults(func=edit)

    subparser_remove: argparse.ArgumentParser = subparsers.add_parser(
        "remove", help="remove a record from the database")
    subparser_remove.add_argument('record_no', metavar="record-no", type=int)
    subparser_remove.set_defaults(func=remove)

    subparser_show: argparse.ArgumentParser = subparsers.add_parser(
        "show", help="show record(s)/record IDs in the database")
    subparser_show.add_argument("--indent", type=int)
    subparser_show.add_argument(
        'record_nos', metavar="record-nos", nargs='*', type=int,
        help="show corresponding records when given, otherwise show the numbers of recorded records")
    subparser_show.set_defaults(func=show)

    return parser.parse_args()


def main() -> int:
    try:
        args: argparse.Namespace = parse_args()
        tx: dataset.Database
        args.func(args)
    except Exception as e:
        print(e, file=sys.stderr)
        return 1 if os.name == 'nt' else os.EX_SOFTWARE
    return 0 if os.name == 'nt' else os.EX_OK
