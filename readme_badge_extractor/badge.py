from typing import NamedTuple, List


class Badge(NamedTuple):
    image_url: str
    image_alt: str = ""
    url: str = ""

    def to_html(self) -> str:
        return f'<a href="{self.url}"><img src="{self.image_url}" alt="{self.image_alt}"></a>'


def remove_badge_duplicates(badges: List[Badge]) -> List[Badge]:
    """Remove duplicates among badges. Where for a duplicate, it is enough
    when the url is the same.
    """
    urls = []
    return_badges = []
    for badge in badges:
        if badge.url not in urls:
            return_badges.append(badge)
        urls.append(badge.url)
    return return_badges
