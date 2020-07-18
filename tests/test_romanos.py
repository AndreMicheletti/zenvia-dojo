import pytest


@pytest.fixture(params=[
    (1, "I"),
    (2, "II"),
    (3, "III"),
    (4, "IV"),
    (5, "V"),
    (6, "VI"),
    (7, "VII"),
    (8, "VIII"),
    (9, "IX"),
    (10, "X"),
    (19, "XIX"),
    (40, "XL"),
    (31, "XXXI"),
    (52, "LII"),
    (112, "CXII"),
    (448, "CDXLVIII"),
    (512, "DXII"),
    (999, "CMXCIX"),
    (5423, "MMMMMCDXXIII"),
])
def valid_inputs(request):
    return request.param


def test_arabic_to_roman_conversion(valid_inputs):
    """
    GIVEN: an arabic integer number
    WHEN: converting to roman numeral
    THEN: should return the string format for a roman numeral
    """
    from romanos.convert import convert_arabic_to_roman

    arabic, expected = valid_inputs

    result = convert_arabic_to_roman(arabic)
    assert expected == result, \
        f"'{arabic}' should be converted to '{expected}'," \
        f" but was converted to '{result}' instead"
