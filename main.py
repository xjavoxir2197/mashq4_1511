class Shaxs:
    def ish_kuni_boshlash(self):
        pass

    def maosh_hisoblash(self, soat):
        pass

    def dars_otish(self, fan):
        pass  # default: hech narsa qilmaydi


class Talaba(Shaxs):
    def ish_kuni_boshlash(self):
        return "Talaba darslarga keldi"

    def maosh_hisoblash(self, soat):
        return 0  # talabaga maosh yo‘q


class Oqituvchi(Shaxs):
    def ish_kuni_boshlash(self):
        return "O‘qituvchi darsga tayyor"

    def maosh_hisoblash(self, soat):
        return soat * 50000

    def dars_otish(self, fan):
        return f"{fan} fanidan dars o‘tilmoqda"


class Xodim(Shaxs):
    def ish_kuni_boshlash(self):
        return "Xodim ishga keldi"

    def maosh_hisoblash(self, soat):
        return soat * 30000


# POLIMORFIZM
jamoa = [
    Talaba(),
    Oqituvchi(),
    Xodim()
]

jami = sum([x.maosh_hisoblash(160) for x in jamoa])
print("Umumiy maosh:", jami)
