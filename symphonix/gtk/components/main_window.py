from typing import Any

from gi.repository import Gtk  # type: ignore


def MainWindow(child: Gtk.Widget, title: str, **properties: Any) -> Gtk.ApplicationWindow:
    window = Gtk.ApplicationWindow(**properties)
    window.set_title(title)
    window.set_child(child)
    return window
