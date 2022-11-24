"""List implementation of a set."""

from typing import (
    Generic, Iterable, TypeVar
)

T = TypeVar('T')


class ListSet(Generic[T]):
    """A set of elements of type T."""

    data: list[T]

    def __init__(self, init: Iterable[T]) -> None:
        """Initialise set with init."""
        Set = []
        for i in init:
            if i not in Set:
                Set.append(i)
        self.Set = Set

    def __contains__(self, x: T) -> bool:
        """Test if x is in set."""
        if x in self.Set:
            return True
        else:
            return False

    def __bool__(self) -> bool:
        """
        Return truth value of the set.

        A set is True if it is non-empty and False
        otherwise
        """
        if self.Set == []:
            return False
        else: 
            return True

    def add(self, x: T) -> None:
        """Add x to the set."""
        if x not in self.Set:
            self.Set.append(x)

    def remove(self, x: T) -> None:
        """Remove x from the set."""
        self.Set.remove(x)
