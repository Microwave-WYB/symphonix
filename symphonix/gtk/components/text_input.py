from typing import Callable

from gi.repository import Gtk  # type: ignore

from symphonix.gtk.utils import apply_modifier
from symphonix.modifier import Modifier


def TextInput(
    place_holder: str, on_change: Callable[[str], None], modifier: Modifier | None = None
) -> Gtk.Entry:
    entry = Gtk.Entry()
    entry.set_placeholder_text(place_holder)
    entry.connect("changed", lambda widget: on_change(widget.get_text()))

    if modifier:
        apply_modifier(entry, modifier)

    return entry
