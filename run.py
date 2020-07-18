from romanos.convert import convert_arabic_to_roman


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
