from __future__ import annotations

import importlib.resources
from typing import Optional

import sdk_demo as sdk
import PySide6.QtGui  # This is only for PyInstaller to parse properly
import PySide6.QtXml  # This is only for PyInstaller to parse properly
from PySide6.QtCore import QIODevice, QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QLineEdit, QListWidget, QMainWindow, QPushButton

from .ui import UI
from .. import ui_model


class MainWindow(UI, sdk.Singleton):
    def __init__(self):
        super().__init__(parent=None)
        self.main_window: Optional[QMainWindow] = None
        self.main_window_model: Optional[ui_model.MainWindowModel] = None
        self.datum_list_widget: Optional[QListWidget] = None
        self.add_push_button: Optional[QPushButton]= None
        self.remove_push_button: Optional[QPushButton]= None
        self.save_push_button: Optional[QPushButton]= None
        self.record_no_line_edit: Optional[QLineEdit] = None
        self.lab_no_line_edit: Optional[QLineEdit] = None
        self.rbc_line_edit: Optional[QLineEdit] = None
        self.mcv_line_edit: Optional[QLineEdit] = None
        self.wbc_line_edit: Optional[QLineEdit] = None
        self.hb_line_edit: Optional[QLineEdit] = None
        self.hct_line_edit: Optional[QLineEdit] = None
        self.mch_line_edit: Optional[QLineEdit] = None
        self.mchc_line_edit: Optional[QLineEdit] = None
        self.rdw_cv_line_edit: Optional[QLineEdit] = None
        self.plt_line_edit: Optional[QLineEdit] = None
        self.promyelocyte_line_edit: Optional[QLineEdit] = None
        self.abn_lym_line_edit: Optional[QLineEdit] = None
        self.plasma_cell_line_edit: Optional[QLineEdit] = None
        self.promonocyte_line_edit: Optional[QLineEdit] = None
        self.blast_line_edit: Optional[QLineEdit] = None
        self.abn_mono_line_edit: Optional[QLineEdit] = None
        self.myeloctye_line_edit: Optional[QLineEdit] = None
        self.meta_myelocyte_line_edit: Optional[QLineEdit] = None
        self.band_line_edit: Optional[QLineEdit] = None
        self.segment_line_edit: Optional[QLineEdit] = None
        self.eosinophil_line_edit: Optional[QLineEdit] = None
        self.basophil_line_edit: Optional[QLineEdit] = None
        self.monocyte_line_edit: Optional[QLineEdit] = None
        self.nrbc_line_edit: Optional[QLineEdit] = None
        self.a_lym_line_edit: Optional[QLineEdit] = None
        self.megakaryocyte_line_edit: Optional[QLineEdit] = None

    def bind(self, main_window_model: ui_model.MainWindowModel) -> MainWindow:
        super().bind(main_window_model)

        self.main_window_model = main_window_model

        self.add_push_button = getattr(self.main_window, 'push_button_add')
        self.add_push_button.clicked.connect(self.on_add_push_button_clicked)

        self.remove_push_button = getattr(self.main_window, 'push_button_remove')
        self.remove_push_button.clicked.connect(self.on_remove_push_button_clicked)

        self.save_push_button = getattr(self.main_window, 'push_button_save')
        self.save_push_button.clicked.connect(self.on_save_push_button_clicked)

        self.datum_list_widget = getattr(self.main_window, 'list_widget_datum_list')
        self.datum_list_widget.currentTextChanged.connect(self.on_datum_list_current_text_changed)
        main_window_model.add_on_changed_observer(self.on_datum_list_changed, 'ids')

        self.record_no_line_edit = getattr(self.main_window, 'line_edit_record_no')
        self.record_no_line_edit.textChanged.connect(lambda x: setattr(main_window_model, 'record_no', x))
        main_window_model.add_on_changed_observer(self.on_record_no_changed, 'record_no')

        self.lab_no_line_edit = getattr(self.main_window, 'line_edit_lab_no')
        self.lab_no_line_edit.textChanged.connect(lambda x: setattr(main_window_model, 'lab_no', x))
        main_window_model.add_on_changed_observer(self.on_lab_no_changed, 'lab_no')

        self.mcv_line_edit = getattr(self.main_window, 'line_edit_mcv')
        self.mcv_line_edit.textChanged.connect(lambda x: setattr(main_window_model, 'mcv', x))
        main_window_model.add_on_changed_observer(self.on_mcv_changed, 'mcv')

        self.wbc_line_edit = getattr(self.main_window, 'line_edit_wbc')
        self.wbc_line_edit.textChanged.connect(lambda x: setattr(main_window_model, 'wbc', x))
        main_window_model.add_on_changed_observer(self.on_wbc_changed, 'wbc')

        self.hb_line_edit = getattr(self.main_window, 'line_edit_hb')
        self.hb_line_edit.textChanged.connect(lambda x: setattr(main_window_model, 'hb', x))
        main_window_model.add_on_changed_observer(self.on_hb_changed, 'hb')

        self.hct_line_edit = getattr(self.main_window, 'line_edit_hct')
        self.hct_line_edit.textChanged.connect(lambda x: setattr(main_window_model, 'hct', x))
        main_window_model.add_on_changed_observer(self.on_hct_changed, 'hct')

        return self

    def inflate(self, ui_path: Optional[str] = None) -> MainWindow:
        super().inflate(ui_path)
        with importlib.resources.path(__package__, 'main_window.ui') as main_window_ui:
            main_window_ui_qfile: QFile = QFile(str(main_window_ui))
            if not main_window_ui_qfile.open(QIODevice.ReadOnly):
                raise RuntimeError(f"Cannot open {main_window_ui}: {main_window_ui_qfile.errorString()}")
            qui_loader: QUiLoader = QUiLoader()
            self.main_window = qui_loader.load(main_window_ui_qfile)
            main_window_ui_qfile.close()
            if not self.main_window:
                raise RuntimeError(qui_loader.errorString())
        return self

    def show(self) -> MainWindow:
        super().show()
        self.main_window_model.update_ids()
        self.main_window.show()
        return self

    def on_add_push_button_clicked(self, checked: bool):
        self.main_window_model.create_datum()
        self.datum_list_widget.setCurrentRow(self.datum_list_widget.count() - 1)

    def on_remove_push_button_clicked(self, checked: bool):
        self.main_window_model.remove_datum(int(self.datum_list_widget.currentItem().text()))

    def on_save_push_button_clicked(self, checked: bool):
        self.main_window_model.edit_datum(int(self.datum_list_widget.currentItem().text()))

    def on_datum_list_changed(self, ids: list[int]):
        last_index: int = self.datum_list_widget.currentRow()
        self.datum_list_widget.clear()
        self.datum_list_widget.addItems(map(str, ids))
        self.datum_list_widget.setCurrentRow(
            last_index if 0 <= last_index < self.datum_list_widget.count() else self.datum_list_widget.count() - 1)

    def on_datum_list_current_text_changed(self, id_str: str):
        if not id_str:
            id_str = '-1'
        self.main_window_model.update_datum(int(id_str))

    def on_record_no_changed(self, record_no: str):
        self.record_no_line_edit.setText(record_no)

    def on_lab_no_changed(self, lab_no: str):
        self.lab_no_line_edit.setText(lab_no)

    def on_mcv_changed(self, mcv: str):
        self.mcv_line_edit.setText(mcv)

    def on_wbc_changed(self, wbc: str):
        self.wbc_line_edit.setText(wbc)

    def on_hb_changed(self, hb: str):
        self.hb_line_edit.setText(hb)

    def on_hct_changed(self, hct: str):
        self.hct_line_edit.setText(hct)
