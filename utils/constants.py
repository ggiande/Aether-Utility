import os
import tarfile
import shutil
import typing

from typing import List, Set, Dict, Final


class Constants:
    """
    Utility stores global constants, per use, make sure to use .copy()  to NOT change the original value
    """
    DEFAULT_ENTRY_ROW: Final[List[str]] = ["DEFAULT_ENTRY"]
    DEFAULT_ENTRY_COLUMNS: Final[List[str, str]] = ["DEFAULT_COL_NAME", "DEFAULT_COL_NAME"]

    def __init__(self) -> None:
        """
        Special method that replaces a constructor/__new()__
        """