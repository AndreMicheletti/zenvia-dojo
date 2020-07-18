import pytest


@pytest.fixture(params=[
    (10000, ValueError),
    (60000, ValueError),
    ("a", TypeError),
    ([], TypeError),
    (12.1, TypeError),
    ({}, TypeError),
    (False, TypeError),
    (lambda x: x, TypeError)
])
def invalid_inputs(request):
    return request.param


def test_invalid_inputs_arabic_to_roman_conversion(invalid_inputs):
    """
    GIVEN: an invalid input
    WHEN: converting to roman numeral
    THEN: should raise ValueError or TypeError
    """
    from romanos.convert import convert_arabic_to_roman

    i_input, error_raised = invalid_inputs

    with pytest.raises(error_raised):
        convert_arabic_to_roman(i_input)
