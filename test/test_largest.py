from largest import LargestNumber as ln


class Testing:
    def test_largestNumber1(self):
        assert ln.largestNumber(self, 1, 2) == 2 # type: ignore

    def test_largestNumber2(self):
        assert ln.largestNumber(self, 2, 1) == 2 # type: ignore

    def test_largestNumber3(self):
        assert ln.largestNumber(self, 2, 2) == None # type: ignore

    def test_largestNumber4(self):
        assert ln.largestNumber(self, -1, 2) == 2 # type: ignore

    def test_largestNumber5(self):
        assert ln.largestNumber(self, 2, -1) == 2 # type: ignore

    def test_largestNumber6(self):
        assert ln.largestNumber(self, -1, -1) == None # type: ignore

    def test_largestNumber7(self):
        assert ln.largestNumber(self, -1, -2) == -1 # type: ignore

    def test_largestNumber8(self):
        assert ln.largestNumber(self, -2, -1) == -1 # type: ignore

    def test_largestNumber9(self):
        assert type(ln.largestNumber(self, 1, 0)) == int # type: ignore
