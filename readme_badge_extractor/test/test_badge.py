from readme_badge_extractor.badge import Badge, remove_badge_duplicates


def test_badge_to_html():
    assert (
        Badge(image_url="image_url", image_alt="alt", url="url").to_html()
        == '<a href="url"><img src="image_url" alt="alt"></a>'
    )


def test_remove_badge_duplicats():
    a = Badge(url="1", image_url="asdf")
    a2 = Badge(url="2", image_url="asdf")
    b = Badge(url="3", image_url="b")
    b2 = Badge(url="4", image_url="b")
    assert remove_badge_duplicates([a, a2, b, b2]) == [a, b]
