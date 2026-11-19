def them(ds):
    ma = input("Nhap ma: ")
    ten = input("Nhap ten: ")
    for sv in ds:
        if sv["ma"] == ma:
            print("Ma da ton tai")
            return
    ds.append({"ma": ma, "ten": ten})
def xoa(ds):
    ma = input("Nhap ma can xoa: ")
    for sv in ds:
        if sv["ma"] == ma:
            ds.remove(sv)
            return
    print("Khong tim thay")
def sua(ds):
    ma = input("Nhap ma SV can sua: ")
    for sv in ds:
        if sv["ma"] == ma:
            print("1. Sua ma")
            print("2. Sua ten")
            print("3. Sua ca hai")
            chon = input("Chon: ")
            if chon == "1" or chon == "3":
                ma_moi = input("Nhap ma moi: ")
                if any(x["ma"] == ma_moi for x in ds if x is not sv):
                    print("Ma da ton tai")
                    return
                sv["ma"] = ma_moi
            if chon == "2" or chon == "3":
                sv["ten"] = input("Nhap ten moi: ")

            if chon in ("1", "2", "3"):
                print("Sua thanh cong")
            else:
                print("Chon sai")
            return
    print("Khong tim thay")
def xem(ds):
    for sv in ds:
        print(sv["ma"], sv["ten"])
