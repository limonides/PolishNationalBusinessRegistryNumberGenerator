from random import randint, choice
from voivodeships.list import PolishVoivodeship


class PolishNationalBusinessRegistryNumberGenerate:
    regon = []
    weight = (8, 9, 2, 3, 4, 5, 6, 7)

    def __init__(self, how_much):
        self.how_much = how_much

    @staticmethod
    def generate_number():

        elem, office = choice(list(PolishVoivodeship.woj.items()))
        x = [randint(0, 9) for p in range(0, 6)]
        for i in elem[::-1]:
            x.insert(0, int(i))
        if sum([a * b for a, b in zip(PolishNationalBusinessRegistryNumberGenerate.weight, x)]) % 11 != 10:
            x.append(sum([a * b for a, b in zip(PolishNationalBusinessRegistryNumberGenerate.weight, x)]) % 11)
            x = ''.join(map(str, x))
            return x
        else:
            x.append(0)
            x = ''.join(map(str, x))
            return x

    def print_numbers(self):
        for el in range(self.how_much):
            print(str(el+1) + ' - ' + self.generate_number())