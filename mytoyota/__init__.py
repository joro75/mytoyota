"""Toyota Connected Services Client"""
from .client import MyT  # pylint: disable=unused-import # NOQA

try:
    import importlib.metadata as importlib_metadata
except ModuleNotFoundError:
    # 3.7
    import importlib_metadata

try:
    __version__ = importlib_metadata.version(__name__)
except importlib_metadata.PackageNotFoundError:
    pass
