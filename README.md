# Python GUI Application with Database Demo

[![Python GUI Application with Database Demo](http://img.youtube.com/vi/Fae89t8lfgc/0.jpg)](http://www.youtube.com/watch?v=Fae89t8lfgc "Python GUI Application with Database Demo")

## Installation

Install with [pip](https://pip.pypa.io/en/stable/) or download the pre-compiled executable file from [here](https://github.com/changyuheng/python-gui-application-with-database-demo/tags).

```
pip install git+https://github.com/changyuheng/python-gui-application-with-database-demo.git
```

## Usage

```
desktop-demo
```

## Development

### Environment

1. [Python 3.9.2+](https://www.python.org/downloads/release/python-392/)
2. [Poetry](https://python-poetry.org/)
3. [PyCharm](https://www.jetbrains.com/pycharm/)

### Setup

```
pip install poetry
poetry install
```

### Packaging

```
poetry run pyinstaller --add-data packages\desktop_demo\ui\main_window.ui;desktop_demo\ui --onefile .venv\Scripts\desktop-demo
```
   
### Key libraries

1. [dataset](https://dataset.readthedocs.io/en/latest/)
2. [Qt for Python](https://www.qt.io/qt-for-python)

### Design concepts

1. [Object-oriented programming](https://en.wikipedia.org/wiki/Object-oriented_programming)
2. [Model–view–viewmodel (MVVM)](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93viewmodel)

## References

1. [My Python Development Environment, 2020 Edition](https://jacobian.org/2019/nov/11/python-environment-2020/)
