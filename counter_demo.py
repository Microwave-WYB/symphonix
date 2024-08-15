from symphonix.core import MutableState, rs
from symphonix.gtk import Button, Column, MainWindow, Row, Text, TextInput
from symphonix.gtk.decorator import app
from symphonix.layout.alignment import Alignment
from symphonix.layout.arrangement import Arrangement
from symphonix.modifier import Modifier


@app(app_id="com.example.Counter")
def Counter(modifier: Modifier | None = None):
    if modifier is None:
        modifier = Modifier()
    count = MutableState[int](0)
    name = MutableState[str]("World")

    def increment():
        count.set(count.get() + 1)

    def decrement():
        count.set(count.get() - 1)

    def reset_counter():
        count.set(0)

    return MainWindow(
        Column(
            Column(
                Text(
                    content=rs("Count: {0}", count),
                    modifier=Modifier().padding(5),
                ),
                Row(
                    Button(
                        text="Increment",
                        on_click=increment,
                        modifier=Modifier().fill_max_width().padding(5),
                    ),
                    Button(
                        text="Decrement",
                        on_click=decrement,
                        modifier=Modifier().fill_max_width().padding(5),
                    ),
                    Button(
                        text="Reset",
                        on_click=reset_counter,
                        modifier=Modifier().fill_max_width().padding(5),
                    ),
                    Button(
                        text="Surprise",
                        on_click=lambda: count.set(count.get() + 10),
                        modifier=Modifier().fill_max_width().padding(5),
                    ),
                    modifier=Modifier().fill_max_width().padding(5),
                    arrangement=Arrangement.SPACE_EVENLY,
                ),
            ),
            Column(
                Text(
                    content=rs("Hello, {0}!", name),
                    modifier=Modifier().alignment(Alignment.CENTER_START).padding(5, 0),
                ),
                Row(
                    TextInput(
                        "Enter your name",
                        lambda text: name.set(text),
                        modifier=Modifier().fill_max_width().padding(5),
                    ),
                    Button("Reset Name", lambda: name.set("World"), modifier=Modifier().padding(5)),
                    modifier=Modifier().fill_max_width().padding(5),
                ),
                modifier=Modifier().fill_max_width().fill_max_height(),
                arrangement=Arrangement.END,
            ),
            modifier=modifier.fill_max_width(),
        ),
        title="Counter",
    )


if __name__ == "__main__":
    Counter()
