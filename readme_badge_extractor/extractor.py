# std
from abc import ABC, abstractmethod
from typing import List, Union
from pathlib import PurePath, Path
import re
import urllib.request

# ours
from readme_badge_extractor.badge import Badge, remove_badge_duplicates


class Extractor(ABC):
    def __init__(self, **kwargs):
        pass

    def extract_from_url(self, url: str) -> List[Badge]:
        return self.extract_from_string(
            urllib.request.urlopen(url).read().decode()
        )

    def extract_from_file(self, file: Union[str, PurePath]) -> List[Badge]:
        return self.extract_from_string(Path(file).read_text())

    @abstractmethod
    def extract_from_string(self, string: str) -> List[Badge]:
        pass


class DefaultExtractor(Extractor):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.image_badge_regex = re.compile(r"\[!\[(.*)]\(([^)]*)\)]\(([^)]*)\)")

    def extract_from_string(self, string: str) -> List[Badge]:
        return remove_badge_duplicates(
            [
                Badge(image_alt=hit[0], image_url=hit[1], url=hit[2])
                for hit in self.image_badge_regex.findall(string)
            ]
        )
