class LargestNumber:
    def __init__(self) -> None:
        pass

    def largestNumber(self, num1: int, num2: int) -> int | None:
        """Compare 2 integers, return largest number
        if they are the same, None returns

        Args:
            num1 (int): Number 1
            num2 (int): Number 2

        Returns:
            int: Largest number
        """
        result = None
        if num1 > num2:
            result = num1
        elif num2 > num1:
            result = num2
        else:
            result = None
        return result


ln = LargestNumber()

print(ln.largestNumber(2, 1))
print(ln.largestNumber(1, 2))
print(type(ln.largestNumber(2, 2)))
