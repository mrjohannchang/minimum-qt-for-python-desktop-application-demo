from __future__ import annotations

from typing import Optional, TypeVar

from .. import ui_model

Self: type = TypeVar('Self')
T: type = TypeVar('T', bound='UI')
U: type = TypeVar('U', bound=ui_model.UIModel)


class UI:
    def __init__(self: Self, parent: Optional[T] = None):
        self.parent: Optional[T] = parent
        self.children: list[UI] = list()

    def bind(self: Self, model: U) -> Self:
        return self

    def inflate(self: Self, ui_path: Optional[str] = None) -> Self:
        return self

    def show(self: Self) -> Self:
        return self
