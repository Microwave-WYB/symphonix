from typing import Callable

from gi.repository import Gtk  # type: ignore

from symphonix.core import ReactiveString, State
from symphonix.gtk.utils import apply_modifier
from symphonix.modifier import Modifier


def Text(
    content: str | State[str] | ReactiveString, modifier: Modifier | None = None
) -> Callable[[], Gtk.Label]:
    def create_label():
        label = Gtk.Label()

        def update_text():
            if isinstance(content, State):
                label.set_text(str(content.get()))
            elif isinstance(content, ReactiveString):
                label.set_text(content.get())
            else:
                label.set_text(content)

        if isinstance(content, State):
            content.register(lambda _: update_text())
        elif isinstance(content, ReactiveString):
            for state in content.states:
                state.register(lambda _: update_text())

        update_text()

        if modifier:
            apply_modifier(label, modifier)

        return label

    return create_label
