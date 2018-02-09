class hitungBinary():
    def __init__(self, arg1, arg2):
        self.dec1 = arg1
        self.dec2 = arg2

    def tambah(self):
        result = self.dec1 + self.dec2
        return result

    def kurang(self):
        result = self.dec1 - self.dec2
        return result

    def kali(self):
        result = self.dec1 * self.dec2
        return result

    def bagi(self):
        result = self.dec1 / self.dec2
        return result

    def mod(self):
        result = self.dec1 % self.dec2
        return result
