from enum import StrEnum


class Alignment(StrEnum):
    """Alignment of a widget within its parent container."""

    BOTTOM_CENTER = "bottom_center"
    BOTTOM_START = "bottom_start"
    BOTTOM_END = "bottom_end"
    CENTER = "center"
    CENTER_START = "center_start"
    CENTER_END = "center_end"
    TOP_CENTER = "top_center"
    TOP_START = "top_start"
    TOP_END = "top_end"
