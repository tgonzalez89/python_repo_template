"""project_name - top-level package."""

from importlib.metadata import version

__version__: str = version("project_name")

__all__: list[str] = ["__version__"]
