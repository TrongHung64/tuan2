class Time:
    def __init__(self , Hours , Minutes , Senconds , TGio=0 , TPhut=0 , TGiay=0):
        self.Hours = Hours
        self.Minutes = Minutes
        self.Seconds = Senconds
        self.TGio = TGio
        self.TPhut = TPhut
        self.TGiay = TGiay

    def normalize(self):
        # chuan hoa giu lieu gio
        if self.Hours < 0 or self.Hours >= 24:
            for i in range(self.Hours // 24):
                self.Hours = self.Hours - 24
        if self.Minutes < 0 or self.Minutes >= 60:
            for i in range(self.Minutes // 60):
                self.Minutes = self.Minutes - 60
                self.Hours += 1
        if self.Seconds < 0 or self.Seconds >= 60:
            for i in range(self.Seconds // 60):
                self.Seconds = self.Seconds - 60
                self.Minutes += 1

    def advance(self):
        self.Hours += self.TGio
        for i in range(self.Hours // 24):
            if self.Hours >= 24:
                self.Hours -= 24
        self.Minutes += self.TPhut
        for i in range(self.Minutes // 60):
            if self.Minutes >= 60:
                self.Minutes -= 60
                self.Hours += 1
        self.Seconds += self.TGiaySeconds
        for i in range(self.Seconds // 60):
            if self.Seconds >= 60:
                self.Seconds -= 60
                self.Minutes += 1
        return "Thoi Gian Sau Khi Tang la: {} Gio {} phut {} Giay..".format(self.Hours , self.Minutes , self.Seconds)

    def __str__(self):
        return "Hien Tai Dang La {} Gio {} Phut {} Giay".format(self.Hours , self.Minutes , self.Seconds)

    def set_Gio(self , Hours):
        self.Hours = Hours

    def set_Phut(self , Minutes):
        self.Minutes = Minutes

    def set_Giay(self , Seconds):
        self.Seconds = Seconds


def main():
    Hours = int(input("Nhap vao so gio: "))
    Minutes= int(input("Nhap vao so phut: "))
    Seconds= int(input("Nhap vao so giay: "))
    ThoiGian = Time(Hours , Minutes , Seconds)
    print(ThoiGian.normalize( ))
    print(ThoiGian.__str__( ))
    TGio = int(input("Nhap vao so gio muon Them: "))
    TPhut = int(input("Nhap vao so phut muon Them: "))
    TGiay = int(input("Nhap vao so giay muon Them: "))
    ThoiGian = Time(Hours , Minutes , Seconds , TGio , TPhut , TGiay)
    print(ThoiGian.advance( ))


main( )
