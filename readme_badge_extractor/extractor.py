# std
from abc import ABC, abstractmethod
from typing import List, Union
from pathlib import PurePath, Path
import re
import urllib.request

# ours
from readme_badge_extractor.badge import Badge, remove_badge_duplicates
from readme_badge_extractor.util.log import OL, lon


class Extractor(ABC):
    def __init__(self, *, log: OL = None, **kwargs):
        self.log = lon(log)

    def extract_from_url(self, url: str) -> List[Badge]:
        self.log.info(f"Downloading {url}")
        text = urllib.request.urlopen(url).read().decode()
        return self.extract_from_string(text)

    def extract_from_file(self, file: Union[str, PurePath]) -> List[Badge]:
        self.log.info(f"Reading {file}")
        text = Path(file).read_text()
        return self.extract_from_string(text)

    @abstractmethod
    def extract_from_string(self, string: str) -> List[Badge]:
        pass


_is_svg_url_regex = re.compile(r"^.*\.svg\??")


def is_svg_url(url: str) -> bool:
    """Does the URL point to a svg image?"""
    return bool(_is_svg_url_regex.findall(url))


class DefaultExtractor(Extractor):
    def __init__(self, require_svg=True, **kwargs):
        """

        Args:
            require_svg: Only svg images are considered for badges
            **kwargs:
        """
        super().__init__(**kwargs)
        self.require_svg = require_svg
        self.image_badge_regex = re.compile(r"\[!\[(.*)]\(([^)]*)\)]\(([^)]*)\)")

    def extract_from_string(self, string: str) -> List[Badge]:
        badges = [
            Badge(image_alt=hit[0], image_url=hit[1], url=hit[2])
            for hit in self.image_badge_regex.findall(string)
        ]
        if self.require_svg:
            badges = [badge for badge in badges if is_svg_url(badge.url)]
        badges_wo_dupes = remove_badge_duplicates(badges)
        n_duplicates_removed = len(badges) - len(badges_wo_dupes)
        if n_duplicates_removed:
            self.log.debug(f"Removed {n_duplicates_removed} duplicated badges")
        self.log.debug(f"Extracted {len(badges_wo_dupes)} badges")
        return badges_wo_dupes
