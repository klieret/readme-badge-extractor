from typing import NamedTuple


class Badge(NamedTuple):
    image_url: str
    image_alt: str = ""
    url: str = ""

    def to_html(self) -> str:
        pass
