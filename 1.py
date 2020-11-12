from math import sqrt

class HinhcChuNhat:
    def __init__(self, a, b):
        self.chieudai = a
        self.chieurong = b

    def ChuviChuNhat(self):
        print('Chu vi cua hinh chu nhat la', 2 * (self.chieudai + self.chieurong))

    def DientichChuNhat(self):
        print('Dien tich cua hinh chu nhat la', (self.chieudai * self.chieurong))


class HinhTron:
    def __init__(self, a):
        self.bankinh = a

    def ChuviHinhTron(self):
        print('Chu vi cua hinh tron la', 3.14 * self.bankinh * 2)

    def DientichHinhTron(self):
        print('dien tich cua hinh tron la', self.bankinh * self.bankinh * 3.14)


class HinhVuong:
    def __init__(self, a):
        self.canh = a

    def ChuviHinhVuong(self):
        print('Chu vi cua hinh vuong la', self.canh * 4)

    def DientichHinhVuong(self):
        print('Dien tich cua hinh vuong la', self.canh * self.canh)


class HinhTamGiac:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def ChuviTamGiac(self):
        print('Chu vi cua hinh tam giac la', self.a + self.b + self.c)

    def DientichTamGiac(self):
        p = (self.a + self.b + self.c) / 2

        print('Dien tich cua hinh tam giac la', sqrt(p * (p - self.a) * (p - self.b) * (p - self.c)))


def Menu():
    print("\n"
          "    0. Thoat\n"
          "    1. Hinh chu nhat\n"
          "    2. Hinh tron\n"
          "    3. Hinh tam giac\n"
          "    4. Hinh vuong\n"
          "    ")


if __name__ == "__main__":
    luaChon = None
    while luaChon != 0:
        Menu()
        luaChon = int(input('Moi ban nhap lua chon: '))
        if luaChon == 0:
            print(' Ket thuc')
            break
        if luaChon == 1:
            print('Moi ban nhap cac canh hinh chu nhat')
            a = int(input('chieu rong: '))
            b = int(input('chieu dai: '))
            hinh_chu_nhat = HinhcChuNhat(a, b)
            hinh_chu_nhat.ChuviChuNhat()
            hinh_chu_nhat.DientichChuNhat()
        if luaChon == 2:
            print('Moi ban nhap ban kinh hinh tron')
            a = int(input('ban kinh: '))
            hinh_tron= HinhTron(a)
            hinh_tron.ChuviHinhTron()
            hinh_tron.DientichHinhTron()
        if luaChon == 3:
            print('Moi ban nhap canh hinh tam giac')
            a = int(input('canh a: '))
            b = int(input('canh b: '))
            c = int(input('canh c: '))
            hinh_tam_giac = HinhTamGiac(a, b, c)
            hinh_tam_giac.ChuviTamGiac()
            hinh_tam_giac.DientichTamGiac()
        if luaChon == 4:
            print('Moi ban nhap canh hinh vuong')
            a = int(input('canh a: '))
            hinh_vuong = HinhVuong(a)
            hinh_vuong.ChuviHinhVuong()
            hinh_vuong.DientichHinhVuong()
