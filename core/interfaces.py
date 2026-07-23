from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class Runnable(ABC):
    """Base interface for executable components."""

    @abstractmethod
    def run(self, *args: Any, **kwargs: Any) -> Any:
        """Execute the component."""
        raise NotImplementedError
