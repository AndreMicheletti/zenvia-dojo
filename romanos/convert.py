
romans = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}


def read_input() -> int:
    while True:
        input_value = input("Digite um número inteiro: ")
        try:
            return int(input_value)
        except ValueError:
            print(f"'{input_value}' é invalido como número inteiro.\n")


def convert_arabic_to_roman(arabic_number: int) -> str:

    milhares_digit = int(arabic_number / 1000) % 10
    centena_digit = int(arabic_number / 100) % 10
    dezena_digit = int(arabic_number / 10) % 10
    unidade_digit = int(arabic_number / 1) % 10

    converted = ""

    converted += (milhares_digit * "M")
    converted += build_add_and_sub_digit(centena_digit, "C", "D", "M")
    converted += build_add_and_sub_digit(dezena_digit, "X", "L", "C")
    converted += build_add_and_sub_digit(unidade_digit, "I", "V", "X")

    return converted


def build_add_and_sub_digit(
    units: int,
    symbol: str,
    middle_symbol: str,
    next_digit_symbol: str
) -> str:
    if units == 0:
        return ""

    if units > 5:
        if units < 9:
            to_next = units % 5
            return middle_symbol + (symbol * to_next)
        else:
            return symbol + next_digit_symbol
    elif units < 5:
        if units <= 3:
            return units * symbol
        else:
            return symbol + middle_symbol
    else:
        return middle_symbol


if __name__ == "__main__":
    arabic = read_input()
    result = convert_arabic_to_roman(arabic)
    print(result)
