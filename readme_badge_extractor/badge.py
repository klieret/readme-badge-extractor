from typing import NamedTuple, List


class Badge(NamedTuple):
    image_url: str
    image_alt: str = ""
    url: str = ""

    def to_html(self) -> str:
        return f'<a href="{self.url}"><img src="{self.image_url}" alt="{self.image_alt}"></a>'


def remove_badge_duplicates(badges: List[Badge]) -> List[Badge]:
    """Remove badges that share the image url. Order is kept."""
    urls = []
    return_badges = []
    for badge in badges:
        if badge.image_url not in urls:
            return_badges.append(badge)
        urls.append(badge.image_url)
    return return_badges
