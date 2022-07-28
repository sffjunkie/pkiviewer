from typing import Any


def maybe(
    data: dict[Any, Any], path: str = "", default: Any | None = None
) -> Any | None:
    elems = list(reversed(path.split(".")))
    try:
        while elem := elems.pop():
            if elem not in data:
                return default
            elif len(elems) == 0:
                return data[elem]
            else:
                data = data[elem]
    except IndexError:
        return None
