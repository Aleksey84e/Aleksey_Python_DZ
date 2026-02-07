import pytest
from string_utils import StringUtils

string_utils = StringUtils()

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.positive
@pytest.mark.parametrize("input_string, expected", [
        ("   skypro", "skypro"),
        ("  тест  ", "тест  "),
        ("   04 апреля 2025", "04 апреля 2025"),
    ])
def test_trim_positive(input_string, expected):
        assert string_utils.trim(input_string) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_string, expected", [
        ("", ""),
        (" ", ""),
        ("skypro  ", "skypro  "),
    ])
def test_trim_negative_edge_cases(input_string, expected):
        assert string_utils.trim(input_string) == expected

@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
        ("SkyPro", "S", True),
        ("тестовая строка", "ая", True),
        ("04 апреля 2025", " ", True),
    ])
def test_contains_positive(string, symbol, expected):
        assert string_utils.contains(string, symbol) == expected

@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
        ("", "a", False),
        (" ", "  ", False),
        ("SkyPro", "", False),
    ])
def test_contains_negative_edge_cases(string, symbol, expected):
        assert string_utils.contains(string, symbol) == expected

@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
        ("SkyPro", "k", "SyPro"),
        ("тестовый текст", "ый ", "тестовтекст"),
        ("04 апреля 2025", "04 ", "апреля 2025"),
    ])
def test_delete_symbol_positive(string, symbol, expected):
        assert string_utils.delete_symbol(string, symbol) == expected

@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
        ("", "a", ""),
        (" ", "  ", " "),
        ("SkyPro", "X", "SkyPro"),
    ])
def test_delete_symbol_negative_edge_cases(string, symbol, expected):
        assert string_utils.delete_symbol(string, symbol) == expected