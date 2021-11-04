# std
from abc import ABC, abstractmethod
from typing import List, Union, Optional
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
        text = urllib.request.urlopen(url).read().decode()
        n_lines = len(text.split("\n"))
        self.log.info(f"Read {n_lines} lines from {url}")
        return self.extract_from_string(text)

    def extract_from_file(self, file: Union[str, PurePath]) -> List[Badge]:
        text = Path(file).read_text()
        n_lines = len(text.split("\n"))
        self.log.info(f"Read {n_lines} from {file}")
        return self.extract_from_string(text)

    @abstractmethod
    def extract_from_string(self, string: str) -> List[Badge]:
        pass


def is_allowed_extension(
    url: str, allowed_extensions: Optional[List[str]]
) -> bool:
    """Check whether the url points to an image with an allowed extension.

    Args:
        url:
        allowed_extensions: If None, do not check extension

    Returns:
        bool
    """
    if allowed_extensions is None:
        return True
    return url.split("?")[0].split(".")[-1] in allowed_extensions


class DefaultExtractor(Extractor):
    def __init__(self, allowed_extensions: Optional[List[str]] = None, **kwargs):
        """

        Args:
            allowed_extensions: Only images with these extensions are considered
                as badges. If None, do not check extension
            **kwargs:
        """
        super().__init__(**kwargs)
        self.allowed_extensions = allowed_extensions
        self.image_badge_regex = re.compile(r"\[!\[(.*)]\(([^)]*)\)]\(([^)]*)\)")

    def extract_from_string(self, string: str) -> List[Badge]:
        badges = [
            Badge(image_alt=hit[0], image_url=hit[1], url=hit[2])
            for hit in self.image_badge_regex.findall(string)
        ]
        if self.allowed_extensions:
            n_before = len(badges)
            badges = [
                badge
                for badge in badges
                if is_allowed_extension(badge.image_url, self.allowed_extensions)
            ]
            n_removed = n_before - len(badges)
            if n_removed:
                self.log.debug(
                    f"Removed {n_removed} badges because they weren't svg "
                    f"images"
                )
        badges_wo_dupes = remove_badge_duplicates(badges)
        n_duplicates_removed = len(badges) - len(badges_wo_dupes)
        if n_duplicates_removed:
            self.log.debug(f"Removed {n_duplicates_removed} duplicated badges")
        self.log.debug(f"Extracted {len(badges_wo_dupes)} badges")
        if not badges_wo_dupes:
            self.log.warning("Did not find any badges")
        return badges_wo_dupes
