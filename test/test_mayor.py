from mayor import Mayor as m


class Testing:
    def test_mayor2numeros1(self):
        assert m.mayor2numeros(self, 1, 2) == 2

    def test_mayor2numeros2(self):
        assert m.mayor2numeros(self, 2, 1) == 2

    def test_mayor2numeros3(self):
        assert m.mayor2numeros(self, 2, 2) == None

    def test_mayor2numeros4(self):
        assert m.mayor2numeros(self, -1, 2) == 2

    def test_mayor2numeros5(self):
        assert m.mayor2numeros(self, 2, -1) == 2

    def test_mayor2numeros6(self):
        assert m.mayor2numeros(self, -1, -1) == None

    def test_mayor2numeros7(self):
        assert m.mayor2numeros(self, -1, -2) == -1

    def test_mayor2numeros8(self):
        assert m.mayor2numeros(self, -2, -1) == -1

    def test_mayor2numeros9(self):
        assert type(m.mayor2numeros(self, 1, 0)) == int
