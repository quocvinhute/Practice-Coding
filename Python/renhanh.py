# Cấu trúc rẽ nhánh: 4, 7, 10
# 04. Viết code cho nhập ba số thực (a, b, c). Giải và biện luận nghiệm của phương trình bậc hai: ax2 + bx + c = 0.
a = float(input("Nhap a: "))
b = float(input("Nhap b: "))
c = float(input("Nhap c: "))
if a == 0:
    if b == 0:
        if c == 0:
            print("Phuong trinh vo so nghiem")
        else:
            print("Phuong trinh vo nghiem")
    else:
        print("x =", -c / b)
else:
    delta = b**2 - 4*a*c
    if delta < 0:
        print("Phuong trinh vo nghiem")
    elif delta == 0:
        print("Nghiem kep x =", -b / (2*a))
    else:
        x1 = (-b + delta**0.5) / (2*a)
        x2 = (-b - delta**0.5) / (2*a)
        print("x1 =", x1)
        print("x2 =", x2)
# 07. Viết chương trình xác định thứ trong tuần của ngày 1 tháng 1. Thứ trong tuần của ngày 1 tháng 1 đối với một
# năm được tính theo công thức sau:
# day_of_the_week = (year  + floor((year – 1) / 4) – floor((year – 1) / 100) + floor((year – 1) / 400)) % 7
# Kết quả của công thức trên là một số nguyên thể hiện thứ trong tuần. Việc mã hóa thứ sẽ bắt đầu với ngày Chủ nhật
# với số mã hóa là 0. Tương tự, ngày thứ Bảy sẽ có giá trị mã hóa là 6. Hãy sử dụng công thức trên và viết một chương
# trình đọc số năm từ người sử dụng. Chương trình sẽ tính toán và in ra thứ tương ứng với đối ngày 1 tháng 1 của
# năm mà người dùng nhập.
year = int(input("Nhap nam: "))
day = (year + (year-1)//4 - (year-1)//100 + (year-1)//400) % 7
if day == 0:
    print("Chu nhat")
elif day == 1:
    print("Thu hai")
elif day == 2:
    print("Thu ba")
elif day == 3:
    print("Thu tu")
elif day == 4:
    print("Thu nam")
elif day == 5:
    print("Thu sau")
else:
    print("Thu bay")
# 10. Cho phép người dùng nhập vào 5 số a, b, c, d, e. Hãy cho biết trong 5 số vừa nhập có bao nhiêu số âm, bao nhiêu
# số dương, bao nhiêu số bằng 0?
a = float(input("Nhap a: "))
b = float(input("Nhap b: "))
c = float(input("Nhap c: "))
d = float(input("Nhap d: "))
e = float(input("Nhap e: "))
am = 0
duong = 0
khong = 0
for x in (a, b, c, d, e):
    if x < 0:
        am += 1
    elif x > 0:
        duong += 1
    else:
        khong += 1
print("So am:", am)
print("So duong:", duong)
print("So bang 0:", khong)
