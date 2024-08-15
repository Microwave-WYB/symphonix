from typing import Callable


class State[T]:
    """A reactive state that can be observed by other components."""

    def __init__(self, initial: T | Callable[[], T]):
        self._value = initial if not callable(initial) else initial()
        self._compute = initial if callable(initial) else None
        self._observers: list[Callable[[T], None]] = []
        self._dependencies: list[State] = []

    def get(self) -> T:
        if self._compute:
            self._value = self._compute()
        return self._value

    def register(self, observer: Callable[[T], None]) -> None:
        self._observers.append(observer)
        observer(self.get())

    def unregister(self, observer: Callable[[T], None]) -> None:
        self._observers.remove(observer)

    def _notify(self) -> None:
        for observer in self._observers:
            observer(self.get())

    def depends_on(self, *states: "State") -> "State[T]":
        for state in states:
            if state not in self._dependencies:
                self._dependencies.append(state)
                state.register(lambda _: self._notify())
        return self


class MutableState[T](State[T]):
    """Mutable version of State that allows setting the value."""

    def set(self, new_value: T) -> None:
        self._value = new_value
        self._notify()


class ReactiveString:
    """A wrapper around a string that contains reactive states."""

    def __init__(self, format_string: str, *args: State, **kwargs: State) -> None:
        self.format_string = format_string
        self.args = args
        self.kwargs = kwargs
        self.states = []
        self._find_states()

    def _find_states(self) -> None:
        """Find all states in the arguments."""
        for arg in self.args:
            if isinstance(arg, State):
                self.states.append(arg)
        for arg in self.kwargs.values():
            if isinstance(arg, State):
                self.states.append(arg)

    def get(self) -> str:
        """Get the formatted string with resolved states."""
        resolved_args = [arg.get() if isinstance(arg, State) else arg for arg in self.args]
        resolved_kwargs = {
            k: v.get() if isinstance(v, State) else v for k, v in self.kwargs.items()
        }
        return self.format_string.format(*resolved_args, **resolved_kwargs)

    def __str__(self) -> str:
        return self.get()


def rs(format_string: str, *args: State, **kwargs: State) -> ReactiveString:
    """Shortcut function for creating a ReactiveString."""
    return ReactiveString(format_string, *args, **kwargs)
