from readme_badge_extractor.badge import Badge


def test_badge_to_html():
    assert (
        Badge(image_url="image_url", image_alt="alt", url="url").to_html()
        == '<a href="url"><img src="image_url" alt="alt"></a>'
    )
