from typing import Self

from symphonix.layout.alignment import Alignment


class Modifier:
    """A modifier that can be applied to a widget."""

    def __init__(self) -> None:
        self._padding = None
        self._fill_max_width = False
        self._fill_max_height = False
        self._width = None
        self._height = None
        self._weight = None
        self._alignment = None

    def padding(self, *args: int, **kwargs: int) -> Self:
        """Set the padding of the widget."""
        if len(args) == 1:
            self._padding = (args[0], args[0], args[0], args[0])
        elif len(args) == 2:
            self._padding = (args[0], args[1], args[0], args[1])
        elif len(args) == 4:
            self._padding = (args[0], args[1], args[2], args[3])
        elif "left" in kwargs and "top" in kwargs and "right" in kwargs and "bottom" in kwargs:
            self._padding = (kwargs["left"], kwargs["top"], kwargs["right"], kwargs["bottom"])
        else:
            raise ValueError("Invalid padding arguments")
        return self

    def fill_max_width(self) -> Self:
        """Fill the widget to the maximum width"""
        self._fill_max_width = True
        return self

    def fill_max_height(self) -> Self:
        """Fill the widget to the maximum height"""
        self._fill_max_height = True
        return self

    def fill_max_size(self) -> Self:
        """Fill the widget to the maximum size"""
        self._fill_max_width = True
        self._fill_max_height = True
        return self

    def size(self, width: int | None = None, height: int | None = None) -> Self:
        """Set the size of the widget."""
        self._width = width or self._width
        self._height = height or self._height
        return self

    def alignment(self, alignment: Alignment) -> Self:
        """Set the alignment of the widget."""
        self._alignment = alignment
        return self

    def weight(self, weight: int) -> Self:
        """Set the weight of the widget."""
        raise NotImplementedError("Weight is not implemented yet")
        self._weight = weight
        return self
