import dataclasses
import os
from typing import Any, Iterable, Optional

import dacite
import dataset


@dataclasses.dataclass
class Datum:
    id: Optional[int] = None
    record_no: Optional[str] = None
    lab_no: Optional[str] = None
    wbc: Optional[str] = None
    rbc: Optional[str] = None
    hb: Optional[str] = None
    hct: Optional[str] = None
    mcv: Optional[str] = None
    mch: Optional[str] = None
    mchc: Optional[str] = None
    rdw_cv: Optional[str] = None
    plt: Optional[str] = None
    abn_mono: Optional[str] = None
    promonocyte: Optional[str] = None
    abn_lym: Optional[str] = None
    plasma_cell: Optional[str] = None
    blast: Optional[str] = None
    promyelocyte: Optional[str] = None
    myeloctye: Optional[str] = None
    meta_myelocyte: Optional[str] = None
    band: Optional[str] = None
    segment: Optional[str] = None
    eosinophil: Optional[str] = None
    basophil: Optional[str] = None
    lymphocyte: Optional[str] = None
    a_lym: Optional[str] = None
    monocyte: Optional[str] = None
    megakaryocyte: Optional[str] = None
    nrbc: Optional[str] = None


def add_datum(database_path: str, datum: Datum) -> None:
    datum_dict: dict[str, Any] = dataclasses.asdict(datum)
    datum_dict['id'] = None
    tx: dataset.Database
    with dataset.connect(f'sqlite:///{database_path}') as tx:
        datum_table: dataset.Table = tx.create_table('datum') if 'datum' not in tx.tables else tx.get_table('datum')
        datum_table.insert(datum_dict)
        datum_table.create_index(['id'])


def edit_datum(database_path: str, datum: Datum) -> None:
    if not os.path.exists(database_path):
        raise FileNotFoundError("database is absent")
    if not isinstance(datum.id, int):
        raise KeyError("no id provided")
    tx: dataset.Database
    with dataset.connect(f'sqlite:///{database_path}') as tx:
        if 'datum' not in tx.tables:
            raise ValueError('datum table is not in the database yet')
        datum_table: dataset.Table = tx.get_table('datum')
        datum_table.upsert(dataclasses.asdict(datum), ['id'])


def get_data(database_path: str, ids: Iterable[int]) -> Iterable[Datum]:
    if not os.path.exists(database_path):
        raise FileNotFoundError("database is absent")
    if not ids:
        raise ValueError('no id provided')
    tx: dataset.Database
    with dataset.connect(f'sqlite:///{database_path}') as tx:
        if 'datum' not in tx.tables:
            raise ValueError('datum table is not in the database yet')
        statement: str = f'SELECT * FROM datum WHERE {" OR ".join(map(lambda x: "id=" + str(x), ids))};'
        return map(lambda x: dacite.from_dict(data_class=Datum, data=x), tx.query(statement))


def get_datum(database_path: str, id: int) -> Datum:
    if not os.path.exists(database_path):
        raise FileNotFoundError("database is absent")
    tx: dataset.Database
    with dataset.connect(f'sqlite:///{database_path}') as tx:
        if 'datum' not in tx.tables:
            raise ValueError('datum table is not in the database yet')
        datum_table: dataset.Table = tx.get_table('datum')
        res: Optional[dict[str, Any]] = datum_table.find_one(id=id)
        if not res:
            raise ValueError("no such id")
        return dacite.from_dict(data_class=Datum, data=res)


def get_ids(database_path: str) -> Iterable[int]:
    if not os.path.exists(database_path):
        raise FileNotFoundError("database is absent")
    tx: dataset.Database
    with dataset.connect(f'sqlite:///{database_path}') as tx:
        if 'datum' not in tx.tables:
            raise ValueError('datum table is not in the database yet')
        return map(lambda x: int(x.get('id')), tx.query('SELECT id FROM datum;'))


def remove_datum(database_path: str, id: int) -> None:
    if not os.path.exists(database_path):
        raise FileNotFoundError("database is absent")
    tx: dataset.Database
    with dataset.connect(f'sqlite:///{database_path}') as tx:
        if 'datum' not in tx.tables:
            raise ValueError('datum table is not in the database yet')
        datum_table: dataset.Table = tx.get_table('datum')
        if not datum_table.find_one(id=id):
            raise ValueError("no such id")
        datum_table.delete(id=id)
