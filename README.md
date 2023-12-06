# Minimum Qt for Python Desktop Application Demo

**This is only for demonstrating and reference.**

## Usage

```
pdm run desktop-app
```

## Installation

Install with [pipx](https://pipx.pypa.io/stable/installation/)

```
pipx install git+https://github.com/mrjohannchang/minimum-qt-for-python-desktop-application-demo.git
```

## Development

### Design concepts

1. [Object-oriented programming](https://en.wikipedia.org/wiki/Object-oriented_programming)
2. [Model–view–viewmodel (MVVM)](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93viewmodel)

### Environment

1. [Python 3.11+](https://www.python.org/)
2. [Qt for Python](https://doc.qt.io/qtforpython)
3. [PDM](https://pdm-project.org/)
4. [Git](https://git-scm.com/)

### Setup

```
pdm install
```

### Packaging

#### CLI app

```
pdm run pyinstaller --clean cli-demo.spec
```

#### Desktop app

```
pdm run pyinstaller --clean desktop-demo.spec
```

### Step by step reference

1. Create an empty project with [Git](https://git-scm.com/).

    ```
    git init
    ```

2. Initialize the Python project with [PDM](https://pdm-project.org/). I personally prefer the project to be based on [PEP 582 – Python local packages directory](https://peps.python.org/pep-0582/) instead of [PEP 405 – Python Virtual Environments](https://peps.python.org/pep-0405/).

    ```
    pdm init
    ```

3. Add [Qt for Python](https://doc.qt.io/qtforpython) as a dependent library.

    ```
    pdm add PySide6
    ```

## License

[Mozilla Public License Version 2.0](https://www.mozilla.org/en-US/MPL/2.0/)
