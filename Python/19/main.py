import sinhvien

ds = []

while True:
    print("1.Them  2.Xoa  3.Sua  4.Xem  0.Thoat")
    chon = input("Chon: ")

    if chon == "1":
        sinhvien.them(ds)
    elif chon == "2":
        sinhvien.xoa(ds)
    elif chon == "3":
        sinhvien.sua(ds)
    elif chon == "4":
        sinhvien.xem(ds)
    elif chon == "0":
        break
    else:
        print("Chon sai")