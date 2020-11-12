from math import sqrt

a = float(input("mời bạn nhập a= "))
b = float(input("mời bạn nhập b= "))
c = float(input("mời bạn nhập c= "))
if a == 0:
    if b == 0:
        if c == 0:
            print("phương trình vô số nghiệm")
        else:
            print("phương trình vô nghiệm")
    else:
        x = -c / b
        print(" phương trình có nghiệm là: " , x)
else:
    d = b * b - 4 * a * c
    if d < 0:
        print("phường trình vô nghiệm")
    elif d == 0:
        x = -b / 2 * a
        print("phương trình có nghiệm kép x=" , x)
    elif d > 0:
        x1 = (-b + sqrt(d)) / (2 * a)
        x2 = (-b - sqrt(d)) / (2 * a)
        print("phương trình có nghiệm x1=" , x1)
        print("phương trình có nghiệm x2=" , x2)
from datetime import date


class QLNV:
    luongcb = 9500000

    def __init__(self , hoten='' , diachi='' , gioitinh='' , namsinh='' , sonamct=0):
        self.hoten = hoten
        self.diachi = diachi
        self.gioitinh = gioitinh
        self.namsinh = namsinh
        self.sonamct = sonamct

    def Nhap(self):
        a = 0
        while a == 0:
            try:
                self.hoten = input('nhập họ tên')
                while self.hoten == '' or self.hoten == ' ':
                    self.hoten = input('họ tên không được để trống: ')
                a = 1
            except:
                a = 0
        a = 0
        while a == 0:
            try:
                self.diachi = input('nhập địa chỉ')
                while self.diachi == '' or self.diachi == ' ':
                    self.diachi = input('địa chỉ không được để trống')
                a = 1
            except:
                a = 0
        self.gioitinh = input('nhập giới tính (nam hoặc nu)')
        while self.gioitinh != 'nam' and self.gioitinh != "nu":
            self.gioitinh = input('nhập lại giới tính:')
        a = 0
        while a == 0:
            try:
                z = int(input('nhập ngày sinh'))
                y = int(input('nhập tháng sinh'))
                x = int(input('nhập năm sinh'))
                self.namsinh = date(x , y , z)
                a = 1
            except ValueError:
                a = 0
                print('nhập lại năm sinh')
        a = 0
        while a == 0:
            try:
                self.sonamct = int(input('nhập số năm công tác'))
                a = 1
            except ValueError:
                a = 0

    def Xuat(self):
        print('họ tên:' , self.hoten)
        print('địa chỉ:' , self.diachi)
        print('giới tính:' , self.gioitinh)
        print('năm sinh:' , self.namsinh)
        print('số năm công tác:' , self.sonamct)


class NHANVIENKD(QLNV):
    def __init__(self , hoten='' , diachi='' , gioitinh='' , namsinh='' , sonamct=0 , dt=0 , hh=0):
        super( ).__init__(hoten , diachi , gioitinh , namsinh , sonamct)
        self.hh = hh
        self.dt = dt

    def Nhap(self):
        super( ).Nhap( )
        a = 0
        while a == 0:
            try:
                self.hh = float(input('nhập % hoa hồng:'))
                a = 1
            except:
                a = 0
        a = 0
        while a == 0:
            try:
                self.dt = float(input('nhập doanh thu'))
                a = 1
            except:
                a = 0

    def Xuat(self):
        super( ).Xuat( )
        print('% hoa hồng:' , self.hh)
        print('doanh thu:' , self.dt)
        print('tổng lương' , self.Tongluong( ))

    def Tongluong(self):
        return self.luongcb + self.dt * (self.hh / 100)


class NHANVIENVP(QLNV):
    def __init__(self , hoten='' , diachi='' , gioitinh='' , namsinh='' , sonamct=0 , hsl=0):
        super( ).__init__(hoten , diachi , gioitinh , namsinh , sonamct)
        self.hsl = hsl

    def Nhap(self):
        super( ).Nhap( )
        a = 0
        while a == 0:
            try:
                self.hsl = float(input('nhập hệ số lương:'))
                a = 1
            except:
                a = 0

    def Xuat(self):
        super( ).Xuat( )
        print('hệ số lương:' , self.hsl)
        print('tổng lương' , self.Tongluong( ))

    def Tongluong(self):
        if self.sonamct < 10:
            return self.luongcb * self.hsl + self.luongcb
        else:
            return self.luongcb * self.hsl + 1.2 * self.luongcb


class CONGNHAN(QLNV):
    def __init__(self , hoten='' , diachi='' , gioitinh='' , namsinh='' , sonamct=0 , hsl=0 , sl=0):
        super( ).__init__(hoten , diachi , gioitinh , namsinh , sonamct)
        self.hsl = hsl
        self.sl = sl

    def Nhap(self):
        super( ).Nhap( )
        a = 0
        while a == 0:
            try:
                self.hsl = float(input('nhập hệ số lương:'))
                a = 1
            except:
                a = 0
        a = 0
        while a == 0:
            try:
                self.sl = float(input('nhập sản lượng'))
                a = 1
            except:
                a = 0

    def Xuat(self):
        super( ).Xuat( )
        print('hệ số lương:' , self.hsl)
        print('sản lượng:' , self.sl)
        print('tổng lương' , self.Tongluong( ))

    def Tongluong(self):
        if self.sl < 1000:
            return self.luongcb * self.hsl + self.luongcb
        else:
            return self.luongcb * self.hsl + self.luongcb * 1.5


def ngtrang():
    print('*' * 25)


def HT(list , a):
    for obj in list:
        if obj.hoten == a:
            obj.Xuat( )
    ngtrang( )


def Nam(list , a):
    for obj in list:
        if obj.namsinh.year == a:
            obj.Xuat( )
    ngtrang( )


def Tong(list , a):
    b = 0
    for obj in list:
        if obj.namsinh.year == a and obj.diachi == 'thai nguyen':
            b += 1
    return b


def LTB(list):
    b = 0
    c = 0
    for obj in list:
        b += obj.Tongluong( )
        c += 1
    return b / c


def DLTB(list , a):
    for obj in list:
        if obj.Tongluong( ) < a:
            obj.Xuat( )
    ngtrang( )


def menu():
    print('''
    0.kết thúc chương trình
    1.nhập thông tin nhân viên văn phòng
    2.nhập thông tin nhân viên kinh doanh
    3.nhập thông tin công nhân
    4.xuất tất cả các thông tin đã nhập
    5.tìm kiếm theo họ tên
    6.hiện thi tất cả sinh năm 1975
    7.tổng số nhân viên sinh năm 1975 va ở thái nguyên là
    8.hiện thị tất cả nhân viên có lương dưới 5000000
    ''')


def main():
    listVP = [ ]
    listKD = [ ]
    listCN = [ ]
    luaChon = None
    menu( )
    ngtrang( )
    while luaChon != 0:
        a = 0
        while a == 0:
            try:
                luaChon = int(input('nhập lựa chọn:'))
                a = 1
            except:
                a = 0
                ngtrang( )
        ngtrang( )
        if luaChon == 1:
            obj = NHANVIENVP( )
            obj.Nhap( )
            listVP.append(obj)
            ngtrang( )
        elif luaChon == 2:
            obj = NHANVIENKD( )
            obj.Nhap( )
            listKD.append(obj)
            ngtrang( )
        elif luaChon == 3:
            obj = CONGNHAN( )
            obj.Nhap( )
            listCN.append(obj)
            ngtrang( )
        elif luaChon == 4:
            a = len(listVP)
            b = len(listKD)
            c = len(listCN)
            if a == 0 or b == 0 or c == 0:
                print('mời nhập đủ nhân viên của các ban')
                ngtrang( )
            else:
                print('danh sách văn phòng')
                for obj in listVP:
                    obj.Xuat( )
                ngtrang( )
                print('danh sách kinh doanh')
                for obj in listKD:
                    obj.Xuat( )
                ngtrang( )
                print('danh sách công nhân')
                for obj in listCN:
                    obj.Xuat( )
                ngtrang( )
        elif luaChon == 5:
            a = input('tên cần tìm:')
            ngtrang( )
            print('luaChon danh sách văn phòng')
            HT(listVP , a)
            print('luaChon danh sách kinh doanh')
            HT(listKD , a)
            print('luaChon danh sách công nhân')
            HT(listCN , a)
        elif luaChon == 6:
            a = 1975
            print('luaChon danh sách văn phòng')
            Nam(listVP , a)
            print('luaChon danh sách kinh doanh')
            Nam(listKD , a)
            print('luaChon danh sách công nhân')
            Nam(listCN , a)
        elif luaChon == 7:
            a = 1975
            b = Tong(listVP , a)
            c = Tong(listKD , a)
            d = Tong(listCN , a)
            print('tổng số nhân viên có năm sinh trên là:' , b + c + d)
            ngtrang( )
        elif luaChon == 8:
            a = 5000000
            print('trung bình lương là:' , a)
            ngtrang( )
            print('mức lương dưới trung bình là')
            print('luaChon danh sách văn phòng')
            DLTB(listVP , a)
            print('luaChon danh sách kinh doanh')
            DLTB(listKD , a)
            print('luaChon danh sách công nhân')
            DLTB(listCN , a)
        elif luaChon == 0:
            print('kết thúc chương trình tạm biệt.')
            ngtrang( )


main( )
