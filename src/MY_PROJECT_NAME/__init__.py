"""MY_PROJECT_NAME – top-level package."""

from importlib.metadata import version

__version__: str = version("MY_PROJECT_NAME")

__all__: list[str] = ["__version__"]
