from typing import Callable

from gi.repository import Gtk  # type: ignore

from symphonix.gtk.utils import apply_modifier
from symphonix.modifier import Modifier


def Button(
    text: str, on_click: Callable[[], None], modifier: Modifier | None = None
) -> Callable[[], Gtk.Button]:
    def create_button():
        btn = Gtk.Button(label=text)
        btn.connect("clicked", lambda _: on_click())

        if modifier:
            apply_modifier(btn, modifier)

        return btn

    return create_button
