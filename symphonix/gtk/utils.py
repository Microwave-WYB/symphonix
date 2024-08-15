from functools import wraps
from typing import Callable, Optional

import gi
from gi.repository import Gtk  # type: ignore

from symphonix.gtk.components.main_window import MainWindow
from symphonix.layout.alignment import Alignment
from symphonix.layout.arrangement import Arrangement
from symphonix.modifier import Modifier

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")

ComponentType = Gtk.Widget | list[Gtk.Widget] | Callable[[], Gtk.Widget | list[Gtk.Widget]]


def apply_arrangement(box: Gtk.Box, arrangement: Arrangement):
    orientation = box.get_orientation()
    align_box = box.set_halign if orientation == Gtk.Orientation.HORIZONTAL else box.set_valign
    match arrangement:
        case Arrangement.START:
            align_box(Gtk.Align.START)
        case Arrangement.END:
            align_box(Gtk.Align.END)
        case Arrangement.CENTER:
            align_box(Gtk.Align.CENTER)
        case Arrangement.SPACE_BETWEEN:
            box.set_homogeneous(False)
            box.set_spacing(0)
        case Arrangement.SPACE_AROUND:
            box.set_homogeneous(True)
            box.set_spacing(10)
        case Arrangement.SPACE_EVENLY:
            box.set_homogeneous(True)
            box.set_spacing(0)
        case _:
            raise ValueError("Invalid arrangement")


def apply_modifier(widget: Gtk.Widget, modifier: Modifier):
    if modifier._padding:
        widget.set_margin_start(modifier._padding[0])
        widget.set_margin_top(modifier._padding[1])
        widget.set_margin_end(modifier._padding[2])
        widget.set_margin_bottom(modifier._padding[3])

    if modifier._fill_max_width:
        widget.set_hexpand(True)

    if modifier._fill_max_height:
        widget.set_vexpand(True)

    if modifier._width:
        widget.set_size_request(modifier._width, -1)

    if modifier._height:
        widget.set_size_request(-1, modifier._height)

    if modifier._alignment:
        match modifier._alignment:
            case Alignment.BOTTOM_CENTER:
                widget.set_valign(Gtk.Align.END)
            case Alignment.BOTTOM_START:
                widget.set_valign(Gtk.Align.END)
                widget.set_halign(Gtk.Align.START)
            case Alignment.BOTTOM_END:
                widget.set_valign(Gtk.Align.END)
                widget.set_halign(Gtk.Align.END)
            case Alignment.CENTER:
                widget.set_valign(Gtk.Align.CENTER)
            case Alignment.CENTER_START:
                widget.set_valign(Gtk.Align.CENTER)
                widget.set_halign(Gtk.Align.START)
            case Alignment.CENTER_END:
                widget.set_valign(Gtk.Align.CENTER)
                widget.set_halign(Gtk.Align.END)
            case Alignment.TOP_CENTER:
                widget.set_valign(Gtk.Align.START)
            case Alignment.TOP_START:
                widget.set_valign(Gtk.Align.START)
                widget.set_halign(Gtk.Align.START)
            case Alignment.TOP_END:
                widget.set_valign(Gtk.Align.START)
                widget.set_halign(Gtk.Align.END)
            case _:
                raise ValueError("Invalid alignment")


def add_to_container(
    container: Gtk.Box, item: Gtk.Widget | list[Gtk.Widget], modifier: Optional[Modifier] = None
):
    if isinstance(item, Gtk.Widget):
        if modifier:
            apply_modifier(item, modifier)
        container.append(item)
    elif isinstance(item, list):
        for widget in item:
            if isinstance(widget, Gtk.Widget):
                if modifier:
                    apply_modifier(widget, modifier)
                container.append(widget)


def run_app(main_window: Gtk.ApplicationWindow) -> None:
    def on_activate(app):
        main_window.set_application(app)
        main_window.present()

    app = Gtk.Application(application_id="com.example.MyApp")
    app.connect("activate", on_activate)
    app.run(None)
