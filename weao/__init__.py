from typing import Tuple

from .client import Client
from .status import Status
from .exploit import *
from .errors import *

__all__: Tuple[str, ...] = (
    "Client",
    "Status",
)

__version_ = "1.0.0"
__license__ = "MIT"
__author__ = "Ghoul"
