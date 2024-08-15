from functools import wraps

from gi.repository import Gtk  # type: ignore

from symphonix.gtk.components.main_window import MainWindow


def app(app_id="com.example.MyApp"):
    def decorator(component_func):
        @wraps(component_func)
        def wrapper(*args, **kwargs):
            main_window = component_func(*args, **kwargs)
            if not isinstance(main_window, Gtk.ApplicationWindow):
                main_window = MainWindow(main_window, title="Untitled")

            def on_activate(app):
                main_window.set_application(app)
                main_window.present()

            gtk_app = Gtk.Application(application_id=app_id)
            gtk_app.connect("activate", on_activate)
            gtk_app.run(None)

        return wrapper

    return decorator
