print("Mời bạn nhập:")
s = input()
print("Bạn đã nhập:", s)
print("Kiểu dữ liệu:", type(s))

print("Mời bạn nhập:")
s = input()
print("Bạn đã nhập:", s)
print("Kiểu dữ liệu:", type(s))
#input nhập gì cũng ra là kiểu chuỗi

#Viết chương trình cho phép người dùng nhập vào số lượng và đơn giá của một sản phẩm. Xuất lên màn hình tổng tiền trước thuế, tiền thuế 10%, tổng tiền sau

thue = 0.1
don_gia = float(input("Nhap don gia : "))
so_luong = int(input("Nhập soLuong: "))
truoc_thue= don_gia*so_luong
thue =truoc_thue*thue
sau_thue=truoc_thue+thue
print("Tong tien truoc thue:", truoc_thue)
print("Tien thue: ", thue)
print("Tong tien sau thue:", sau_thue)

#Viết chương trình cho phép người dùng nhập vào 3 số nguyên. Tính giá trị trung bình của 3 số vừa nhập
a=int(input("Nhập so nguyen: "))
b=int(input("Nhập so nguyen: "))
c=int(input("Nhập so nguyen: "))
trung_binh= (a+b+c) / 3
trung_binh=int(trung_binh*10)/10
print(trung_binh)

#Viết chương trình nhập một số nguyên gồm 3 chữ số, giả sử luôn nhập đúng. Xuất trung bình cộng ba chữ số của số nguyên đó: hàng trăm, hàng chục, hàng đơn vị.
a=int(input("Nhập so co 3 chu so: "))
x=a//100
y=(a//10)%10
z=a%10
trung_binh=(x+y+z)/3
print(f"{trung_binh:.2f}")

so_xe = int(input("Nhập so xe: "))
x = so_xe//10000
y = (so_xe//1000)%10
z = (so_xe//100)%10
a = (so_xe//10)%10
b = so_xe%10
tong = x+y+z+a+b
nut = tong%10
print(nut)