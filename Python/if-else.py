#thang trong nam nhuan k nhuan
thang = int(input("Nhap thang: "))
nam = int(input("Nhap nam: "))
if thang < 1 or thang > 12 or nam <= 0:
    print("Thang nam khong hop le")
else:
    if thang == 1 or thang == 3 or thang == 5 or thang == 7 or thang == 8 or thang == 10 or thang == 12:
        print("Thang co 31 ngay")
    elif thang == 4 or thang == 6 or thang == 9 or thang == 11:
        print("Thang co 30 ngay")
    else:
        if (nam % 4 == 0 and nam % 100 != 0) or nam % 400 == 0:
            print("Thang co 29 ngay")
        else:
            print("Thang co 28 ngay")

#diem
diem = input("Nhap diem: ")
if diem == 'A+' or diem =='A':
  print(4.0)
elif diem == 'A-':
  print(3.7)
elif diem == 'B+':
  print(3.3)
elif diem == 'B':
  print(3.0)
elif diem == 'B-':
  print(2.7)
elif diem == 'C+':
  print(2.3)
elif diem == 'C':
  print(2.0)
elif diem == 'C-':
  print(1.7)
elif diem == 'D+':
  print(1.3)
elif diem == 'D':
  print(1.0)
elif diem == 'F':
  print(0)
else:
  print("Nhap lai")

#
k = int(input("Nhap k: "))
if k <= 0:
    print("Vui long nhap so nguyen duong")
else:
    for i in range(1, k + 1):
        n = i
        print(n, end="")
        while n != 1:
            if n % 2 == 0:
                n = n // 2
            else:
                n = 3 * n + 1
            print(",", n, sep="", end="")
        print()