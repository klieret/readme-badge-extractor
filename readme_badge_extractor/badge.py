from typing import Dict, NamedTuple, List


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


def badges_to_serializable(badges: List[Badge]) -> List[Dict[str, str]]:
    """Turns list of namedtuples into list of dictionaries"""
    return [dict(badge._asdict()) for badge in badges]


def serialize_badges(badges: List[Badge], format="json") -> str:
    """Turn list of badges into serialized string."""
    if format == "json":
        import json
        return json.dumps(badges_to_serializable(badges))
    elif format == "yaml":
        import yaml
        return yaml.dump(badges_to_serializable(badges))
    else:
        raise ValueError(
            "Only yaml and json format are supported at the moment"
        )