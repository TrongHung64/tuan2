import math

class Phanso:
    def __init__(self , T , M):
        self.T = T
        self.M = M
        # tao cac ham set de thay doi, nhap gia tri

    def set_T(self , T):
        self.T = T
        # tao cac ham get de xuat gia tri

    def get_T(self):
        return self.T

    def set_M(self , M):
        self.M = M

    def get_M(self):
        return self.M

    def __add__(self , other):
        return Phanso((self.T * other.M + self.M * other.T) , (self.M * other.M))

    def __sub__(self , other):

        return Phanso((self.T * other.M - self.M * other.T) , (self.M * other.M))

    def __mul__(self , other):
        return Phanso((self.T * other.T) , (self.M * other.M))

    def __truediv__(self , other):
        return Phanso((self.T * other.M) , (self.M * other.T))

    # Tao ham toi gian de toi gian cac tu,va mau so
    def __str__(self):
        self.Toigian( )
        return " {}/{}".format(self.T , self.M)

    def Toigian(self):
        u = math.gcd(self.T , self.M)
        self.T = self.T / u
        self.M = self.M / u
        return self.T , self.M

    def sosanh(self , other):
        x = (self.T / self.M)
        y = (other.T / other.M)
        if x == y:
            return "2 Phan So Bang Nhau"
        if x < y:
            return "Phan So {}/{} Lon Hon".format(other.T , other.M)
        else:
            return "Phan So {}/{} Lon Hon".format(self.T , self.M)





def main():
    print("--1 Cong: ----------------")
    print("--2 Tru: -----------------")
    print("--3 Nhan: ----------------")
    print("--4 Chia: ----------------")
    print("--5 So Sanh: -------------")
    n = int(input("Nhap Vao Lua Chon Ban Muon: "))
    a = int(input("Nhap Tu Thu Nhat:"))
    b = int(input("Nhap Mau Thu Nhat:"))
    c = int(input("Nhap Tu Thu Hai:"))
    d = int(input("Nhap Mau Thu Hai:"))
    a1 = Phanso(a , b)
    a2 = Phanso(c , d)
    if n == 1:
        print(a1 + a2)
    if n == 2:
        print(a1 - a2)
    if n == 3:
        print(a1 * a2)
    if n == 4:
        print(a1 / a2)
    if n == 5:
        print(a1.sosanh(a2))


main( )
