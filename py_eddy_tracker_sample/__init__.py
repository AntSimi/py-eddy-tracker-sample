from os import path


def get_demo_path(name):
    return path.join(path.dirname(__file__), name)


from ._version import get_versions

__version__ = get_versions()["version"]
del get_versions
