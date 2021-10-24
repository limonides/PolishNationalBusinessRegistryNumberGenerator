from functions.pnbrng import PolishNationalBusinessRegistryNumberGenerate as pnbrng

how = None
while not isinstance(how, int):
    try:
        how = int(input('Podaj liczbę numerów REGON do wygenerowania: '))
    except ValueError as error:
        print('Podana wartość nie jest liczbą. Spróbuj ponownie.')
        continue

numbers = pnbrng(how)
numbers.print_numbers()