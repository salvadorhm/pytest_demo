class Mayor:
    def __init__(self) -> None:
        pass

    def mayor2numeros(self, numero1: int, numero2: int) -> int:
        result = None
        if numero1 > numero2:
            result = numero1
        elif numero2 > numero1:
            result = numero2
        else:
            result = None
        return result


objeto = Mayor()

print(type(objeto.mayor2numeros(2, 1)))
print(type(objeto.mayor2numeros(1, 2)))
print(type(objeto.mayor2numeros(2, 2)))
