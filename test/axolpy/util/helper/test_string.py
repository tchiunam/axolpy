from axolpy.util.helper import string


def test_camelcase_to_underscrollsep() -> None:
    """
    Test to convert a string from camelcase to underscroll sepearated.
    """

    assert string.camelcase_to_underscrollsep("TestString") == "test_string"
    assert string.camelcase_to_underscrollsep(
        "anotherTestString") == "another_test_string"


def test_expand_range() -> None:
    """
    Test to expand all ranges in a string.
    """

    assert list(string.expand_range("1-3,5,7-9")) == [1, 2, 3, 5, 7, 8, 9]


def test_increase_number_in_string() -> None:
    """
    Test to increase numbers in a string.
    """

    assert string.increase_number_in_string(
        "a9k0zk482bm2l82", 1) == "a10k1zk483bm3l83"
    assert string.increase_number_in_string(
        "I put 2 apples in 1 jar", 1) == "I put 3 apples in 2 jar"


def test_get_string_hex() -> None:
    """
    Test to get hashed value of a string.
    """

    assert string.get_string_hex(
        "a test string") == "b1a4cf30d3f4095f0a7d2a6676bcae77"


def test_multiple_replace() -> None:
    """
    Test to replace multiple strings in a string.
    """

    assert string.multiple_replace("Python is a high-level, interpreted, general-purpose programming language",
                                   {"Python": "C", "high-level": "low-level", "interpreted": "compiled"}) == "C is a low-level, compiled, general-purpose programming language"
