
romans_symbols_by_unit = {
    "unidade": ("I", "V", "X"),
    "dezena": ("X", "L", "C"),
    "centena": ("C", "D", "M")
}


def convert_arabic_to_roman(
    arabic_number: int
) -> str:
    """
    Function to convert arabic numeral to roman numeral
    :param arabic_number: (int) value to be converted
    :return: (str) converted value to roman numeral
    """

    if arabic_number > 9999:
        raise ValueError("Can't convert numbers greater than 9999")
    if not isinstance(arabic_number, int) or isinstance(arabic_number, bool):
        raise TypeError("Can't convert values other than integers")

    # extract each digit from the number
    milhares_digit = int(arabic_number / 1000) % 10
    centenas_digit = int(arabic_number / 100) % 10
    dezenas_digit = int(arabic_number / 10) % 10
    unidade_digit = int(arabic_number / 1) % 10

    milhares_romano = (milhares_digit * "M")
    centenas_romano = apply_roman_digit_logic(centenas_digit, *romans_symbols_by_unit["centena"])
    dezenas_romano = apply_roman_digit_logic(dezenas_digit, *romans_symbols_by_unit["dezena"])
    unidades_romano = apply_roman_digit_logic(unidade_digit, *romans_symbols_by_unit["unidade"])

    romano = milhares_romano + centenas_romano + dezenas_romano + unidades_romano
    return romano


def apply_roman_digit_logic(
    digit: int,
    symbol: str,
    middle_symbol: str,
    next_digit_symbol: str
) -> str:
    """
     Apply the Roman addition and subtration logic using the given
    symbols, depending on the unit needed
    :param digit: the digit value for this unit
    :param symbol: the symbol for this unit that represents '1'
    :param middle_symbol: the symbol for this that represents '5'
    :param next_digit_symbol: the symbol for the next unit (represents '10')
    :return: the roman numeral to represent the digit on the given unit
    """
    if digit == 0:
        return ""

    if digit == 5:
        # for example: V
        return middle_symbol
    if digit > 5:
        if digit == 9:
            # for example, IX
            return symbol + next_digit_symbol
        else:
            to_next = digit % 5
            # for example, VII
            return middle_symbol + (symbol * to_next)
    elif digit < 5:
        if digit == 4:
            # for example, IV
            return symbol + middle_symbol
        else:
            # for example, III
            return digit * symbol


def read_input() -> int:
    while True:
        input_value = input("Digite um número inteiro: ")
        try:
            return int(input_value)
        except ValueError:
            print(f"'{input_value}' é invalido como número inteiro.\n")


if __name__ == "__main__":
    arabic = read_input()
    result = convert_arabic_to_roman(arabic)
    print(result)
