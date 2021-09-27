# std
import re
from abc import ABC, abstractmethod

# ours
from readme_badge_extractor.extractor import Extractor
from readme_badge_extractor.util.log import lon, OL


class Includer(ABC):
    def __init__(self, *, log: OL = None, **kwargs):
        self.log = lon(log)

    @abstractmethod
    def include_in_string(self, extractor: Extractor, string) -> str:
        pass


class DefaultIncluder(Includer):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.replace_regex = re.compile(
            r"([\t ]*)<!--\s*README-BADGES-START(.*?)\s*-->(.*?)<!--\s*README-BADGES-END\s*-->",
            flags=re.DOTALL,
        )

    def include_in_string(self, extractor: Extractor, string) -> str:
        for found in self.replace_regex.findall(string):
            indent = found[0]
            url = found[1].strip()
            content = found[2]
            print(content.__repr__())
            badges = extractor.extract_from_url(url)
            badges_str = (
                "\n"
                + "\n".join([indent + badge.to_html() for badge in badges])
                + "\n"
            )
            string = string.replace(content, badges_str)
        return string
