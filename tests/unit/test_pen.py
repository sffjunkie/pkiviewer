from pkiviewer.oid.pen import load_numbers


def test_load_pen():
    numbers = load_numbers()
    assert numbers
    assert numbers[44947].organization == "Internet Security Research Group"
