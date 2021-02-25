from typing import Any, Callable, TypeVar, Union

T: type = TypeVar('T')


class ObservableProperty:
    def __init__(self):
        self._on_changing_observers: list[Callable[[str, Any], None]] = list()
        self._on_specific_changing_observers: dict[str, list[Callable[[Any], None]]] = dict()
        self._on_changed_observers: list[Callable[[str, Any], None]] = list()
        self._on_specific_changed_observers: dict[str, list[Callable[[Any], None]]] = dict()

    def __setattr__(self, name, value):
        if isinstance(getattr(type(self), name, None), property):
            self._on_property_changing(property_name=name, property_value=value)
        super().__setattr__(name, value)
        if isinstance(getattr(type(self), name, None), property):
            self._on_property_changed(property_name=name, property_value=value)

    def _on_property_changing(self, property_name: str, property_value: Any):
        observer: Callable[[str, Any], None]
        for observer in self._on_changing_observers:
            observer(property_name, property_value)

        if property_name in self._on_specific_changing_observers:
            specific_observer: Callable[[Any], None]
            for specific_observer in self._on_specific_changing_observers[property_name]:
                specific_observer(property_value)

    def _on_property_changed(self, property_name: str, property_value: Any):
        observer: Callable[[str, Any], None]
        for observer in self._on_changed_observers:
            observer(property_name, property_value)

        if property_name in self._on_specific_changed_observers:
            specific_observer: Callable[[Any], None]
            for specific_observer in self._on_specific_changed_observers[property_name]:
                specific_observer(property_value)

    def add_on_changing_observer(
            self,
            callable: Union[Callable[[str, Any], None], Callable[[Any], None]],
            property_name: str = ''):
        if property_name:
            if property_name not in self._on_specific_changing_observers:
                self._on_specific_changing_observers[property_name] = list()
            self._on_specific_changing_observers[property_name].append(callable)
        else:
            self._on_changing_observers.append(callable)

    def add_on_changed_observer(
            self,
            callable: Union[Callable[[str, Any], None], Callable[[Any], None]],
            property_name: str = ''):
        if property_name:
            if property_name not in self._on_specific_changed_observers:
                self._on_specific_changed_observers[property_name] = list()
            self._on_specific_changed_observers[property_name].append(callable)
        else:
            self._on_changed_observers.append(callable)

    def remove_on_changing_observer(self, callable: Callable[[str, Any], None]):
        self._on_changing_observers.remove(callable)

    def remove_on_changed_observer(self, callable: Callable[[str, Any], None]):
        self._on_changed_observers.remove(callable)

    def remove_all_on_changing_observers(self):
        self._on_changing_observers.clear()

    def remove_all_on_changed_observers(self):
        self._on_changed_observers.clear()

    def remove_all_observers(self):
        self.remove_all_on_changing_observers()
        self.remove_all_on_changed_observers()


class Singleton:
    _instance: dict[type[T], T] = dict()

    def __call__(cls: type[T], *args, **kwargs) -> T:
        if cls not in cls._instance:
            cls._instance[cls] = super().__call__(*args, **kwargs)
        return cls._instance[cls]
