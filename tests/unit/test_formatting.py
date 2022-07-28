from pkiviewer.view.formatter import int_to_hex_long, bytes_to_hex_long, chunk


def test_int_to_hex_long():
    assert (
        int_to_hex_long(117869795089791359327594732455184760935)
        == "58:ac:e5:94:0b:41:78:64:12:9d:53:1a:39:cb:00:67"
    )


def test_bytes_to_hex_long():
    assert (
        bytes_to_hex_long(
            b"\x58\xac\xe5\x94\x0b\x41\x78\x64\x12\x9d\x53\x1a\x39\xcb\x00\x67"
        )
        == "58:ac:e5:94:0b:41:78:64:12:9d:53:1a:39:cb:00:67"
    )


def test_chunk():
    test_str = "1234567890"
    assert chunk(test_str, 3) == ["123", "456", "789", "0"]
