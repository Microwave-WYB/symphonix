from functools import partial

from gi.repository import Gtk  # type: ignore

from symphonix.gtk.utils import ComponentType, add_to_container, apply_arrangement, apply_modifier
from symphonix.layout.arrangement import Arrangement
from symphonix.layout.orientation import Orientation
from symphonix.modifier import Modifier


def Box(
    *children: ComponentType,
    orientation: Orientation = Orientation.VERTICAL,
    modifier: Modifier | None = None,
    arrangement: Arrangement = Arrangement.SPACE_BETWEEN,
) -> Gtk.Box:
    box = Gtk.Box(
        orientation=Gtk.Orientation.VERTICAL
        if orientation == Orientation.VERTICAL
        else Gtk.Orientation.HORIZONTAL
    )
    if modifier:
        apply_modifier(box, modifier)
    if arrangement:
        apply_arrangement(box, arrangement)
    for child in children:
        if callable(child):
            add_to_container(box, child())
        else:
            add_to_container(box, child)
    return box


Column = partial(Box, orientation=Orientation.VERTICAL)
Row = partial(Box, orientation=Orientation.HORIZONTAL)
Row = partial(Box, orientation=Orientation.HORIZONTAL)
