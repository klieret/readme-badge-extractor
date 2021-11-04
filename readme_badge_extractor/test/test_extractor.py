from readme_badge_extractor.extractor import (
    DefaultExtractor,
    is_allowed_extension,
)


def test_default_extractor_extract_from_url():
    badges = DefaultExtractor().extract_from_url(
        "https://raw.githubusercontent.com/klieret/jekyll-relative-url-check/main/README.md"
    )
    # We know the exact number but it might change so let's just test if we get any
    assert len(badges) >= 1


def test_default_extractor_regex():
    a = "[![Build Status](https://travis-ci.org/klieret/RandomFileTree.svg?branch=master)](https://travis-ci.org/klieret/RandomFileTree)"
    assert DefaultExtractor().image_badge_regex.findall(a) == [
        (
            "Build Status",
            "https://travis-ci.org/klieret/RandomFileTree.svg?branch=master",
            "https://travis-ci.org/klieret/RandomFileTree",
        )
    ]


def test_is_allowed_extension():
    assert is_allowed_extension("asdf/a.svg", None)
    assert is_allowed_extension("asdf/a.svg?a=5", ["svg"])
    assert not is_allowed_extension("asdf/a", ["png"])
    assert is_allowed_extension("", None)
