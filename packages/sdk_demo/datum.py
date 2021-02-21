import dataclasses
import os
from typing import Any, Dict, Iterable, Optional

import dacite
import dataset


@dataclasses.dataclass
class Datum:
    record_no: Optional[int]
    lab_no: Optional[str]
    wbc: Optional[str]
    rbc: Optional[str]
    hb: Optional[str]
    hct: Optional[str]
    mcv: Optional[str]
    mch: Optional[str]
    mchc: Optional[str]
    rdw_cv: Optional[str]
    plt: Optional[str]
    abn_mono: Optional[str]
    promonocyte: Optional[str]
    abn_lym: Optional[str]
    plasma_cell: Optional[str]
    blast: Optional[str]
    promyelocyte: Optional[str]
    myeloctye: Optional[str]
    meta_myelocyte: Optional[str]
    band: Optional[str]
    segment: Optional[str]
    eosinophil: Optional[str]
    basophil: Optional[str]
    lymphocyte: Optional[str]
    a_lym: Optional[str]
    monocyte: Optional[str]
    megakaryocyte: Optional[str]
    nrbc: Optional[str]


def add_datum(database_path: str, datum: Datum):
    if not isinstance(datum.record_no, int):
        raise KeyError("no record number provided")
    tx: dataset.Database
    with dataset.connect(f'sqlite:///{database_path}') as tx:
        datum_table: dataset.Table = tx.create_table('datum') if 'datum' not in tx.tables else tx.get_table('datum')
        if datum_table.find_one(record_no=datum.record_no):
            raise ValueError("duplicated record number")
        datum_table.insert(dataclasses.asdict(datum))
        datum_table.create_index(['record_no'])


def edit_datum(database_path: str, datum: Datum):
    if not os.path.exists(database_path):
        raise FileNotFoundError("database is absent")
    if not isinstance(datum.record_no, int):
        raise KeyError("no record number provided")
    tx: dataset.Database
    with dataset.connect(f'sqlite:///{database_path}') as tx:
        if 'datum' not in tx.tables:
            raise ValueError('datum table is not in the database yet')
        datum_table: dataset.Table = tx.get_table('datum')
        if not datum_table.find_one(record_no=datum.record_no):
            raise ValueError("no such record number")
        datum_table.upsert(dataclasses.asdict(datum), ['record_no'])


def get_data(database_path: str, record_nos: Iterable[int]) -> Iterable[Datum]:
    if not os.path.exists(database_path):
        raise FileNotFoundError("database is absent")
    if not record_nos:
        raise ValueError('no record numbers provided')
    tx: dataset.Database
    with dataset.connect(f'sqlite:///{database_path}') as tx:
        if 'datum' not in tx.tables:
            raise ValueError('datum table is not in the database yet')
        statement: str = f'SELECT * FROM datum WHERE {" OR ".join(map(lambda x: "record_no=" + str(x), record_nos))};'
        return map(lambda x: dacite.from_dict(data_class=Datum, data=x), tx.query(statement))


def get_datum(database_path: str, record_no: int) -> Datum:
    if not os.path.exists(database_path):
        raise FileNotFoundError("database is absent")
    tx: dataset.Database
    with dataset.connect(f'sqlite:///{database_path}') as tx:
        if 'datum' not in tx.tables:
            raise ValueError('datum table is not in the database yet')
        datum_table: dataset.Table = tx.get_table('datum')
        res: Optional[Dict[str, Any]] = datum_table.find_one(record_no=record_no)
        if not res:
            raise ValueError("no such record number")
        return dacite.from_dict(data_class=Datum, data=res)


def get_record_nos(database_path: str) -> Iterable[int]:
    if not os.path.exists(database_path):
        raise FileNotFoundError("database is absent")
    tx: dataset.Database
    with dataset.connect(f'sqlite:///{database_path}') as tx:
        if 'datum' not in tx.tables:
            raise ValueError('datum table is not in the database yet')
        return map(lambda x: int(x.get('record_no')), tx.query('SELECT record_no FROM datum;'))


def remove_datum(database_path: str, record_no: int):
    if not os.path.exists(database_path):
        raise FileNotFoundError("database is absent")
    tx: dataset.Database
    with dataset.connect(f'sqlite:///{database_path}') as tx:
        if 'datum' not in tx.tables:
            raise ValueError('datum table is not in the database yet')
        datum_table: dataset.Table = tx.get_table('datum')
        if not datum_table.find_one(record_no=record_no):
            raise ValueError("no such record number")
        datum_table.delete(record_no=record_no)
