import sdk_demo as sdk

from .ui_model import UIModel


class MainWindowModel(UIModel):
    def __init__(self):
        super().__init__()
        self.datum: sdk.Datum = sdk.Datum()
        self.database_path: str = sdk.default_database
        self._ids: list[int] = list(sdk.get_ids(self.database_path))

    def create_datum(self):
        sdk.add_datum(self.database_path, datum=sdk.Datum())
        self.update_ids()

    def edit_datum(self, id: int):
        sdk.edit_datum(self.database_path, self.datum)

    def remove_datum(self, id: int):
        sdk.remove_datum(self.database_path, id)
        self.update_ids()

    def update_datum(self, id: int):
        datum: sdk.Datum = sdk.get_datum(sdk.default_database, id) if id >= 0 else sdk.Datum()
        self.datum.id = id
        self.record_no = datum.record_no
        self.lab_no = datum.lab_no
        self.mcv = datum.mcv
        self.wbc = datum.wbc
        self.hb = datum.hb
        self.hct = datum.hct

    def update_ids(self):
        self.ids = list(sdk.get_ids(self.database_path))

    @property
    def ids(self) -> list[int]:
        return self._ids

    @ids.setter
    def ids(self, value: list[int]):
        self._ids = value

    @property
    def record_no(self) -> str:
        return self.datum.record_no

    @record_no.setter
    def record_no(self, value: str) -> None:
        self.datum.record_no = value

    @property
    def lab_no(self) -> str:
        return self.datum.lab_no

    @lab_no.setter
    def lab_no(self, value: str) -> None:
        self.datum.lab_no = value

    @property
    def mcv(self) -> str:
        return self.datum.mcv

    @mcv.setter
    def mcv(self, value: str) -> None:
        self.datum.mcv = value

    @property
    def wbc(self) -> str:
        return self.datum.wbc

    @wbc.setter
    def wbc(self, value: str) -> None:
        self.datum.wbc = value

    @property
    def hb(self) -> str:
        return self.datum.hb

    @hb.setter
    def hb(self, value: str) -> None:
        self.datum.hb = value

    @property
    def hct(self) -> str:
        return self.datum.hct

    @hct.setter
    def hct(self, value: str) -> None:
        self.datum.hct = value
