# Cấu trúc lặp: 14

n = int(input("Nhap n: "))
s1 = 0
s2 = 0
s3 = 0
s4 = 0
i = 1
tong = 0
while i <= n:
    tong += i
    s1 += 1 / tong
    s2 += 1 / (i * (i + 1))
    s3 += i / (i + 1)
    i += 1
i = 0
while i <= n:
    s4 += (2*i + 1) / (2*i + 2)
    i += 1
print("S1 =", s1)
print("S2 =", s2)
print("S3 =", s3)
print("S4 =", s4)

