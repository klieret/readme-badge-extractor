from readme_badge_extractor.extractor import DefaultExtractor, is_svg_url


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


def test_is_svg_url():
    assert is_svg_url("asdf/a.svg")
    assert is_svg_url("asdf/a.svg?a=5")
    assert not is_svg_url("asdf/a")
    assert not is_svg_url("")
