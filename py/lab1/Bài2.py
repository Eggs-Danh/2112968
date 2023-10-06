#1
'''
def tinh_phep_tinh(a, b):
    tong = a + b
    thuong = a / b
    luy_thua = a ** b
    return tong, thuong, luy_thua
# Sử dụng hàm để tính các phép tính
a = 10
b = 5
ket_qua = tinh_phep_tinh(a, b)
print("a + b =", ket_qua[0])
print("a / b =", ket_qua[1])
print("a ^ b =", ket_qua[2])
'''
#2 đe thieu nang
'''
def tinh_dien_tich_hinh_chu_nhat(chieu_dai, chieu_rong):
    dien_tich = chieu_dai * chieu_rong
    return dien_tich
# Sử dụng hàm để tính diện tích hình chữ nhật
chieu_dai = 5.0  # Thay thế giá trị này bằng chiều dài thực tế của hình chữ nhật
chieu_rong = 3.0  # Thay thế giá trị này bằng chiều rộng thực tế của hình chữ nhật
dien_tich = tinh_dien_tich_hinh_chu_nhat(chieu_dai, chieu_rong)
print("Diện tích hình chữ nhật là:", dien_tich)
'''
#3
'''
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

start = 10
end = 50

print(f"Các số nguyên tố trong khoảng từ {start} đến {end}:")
for num in range(start, end + 1):
    if is_prime(num):
        print(num)
'''
#4
'''
def la_so_fibonacci(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a == n

# Số bạn muốn kiểm tra
n = 21  # Thay thế số này bằng số bạn muốn kiểm tra

if la_so_fibonacci(n):
    print(f"{n} là số Fibonacci")
else:
    print(f"{n} không phải là số Fibonacci")
'''
#5
'''
# Không đệ quy
def fibonacci_khong_de_quy(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
    
# Số Fibonacci thứ n bạn muốn tìm
n = 10  # Thay thế số này bằng số Fibonacci thứ n bạn muốn
result = fibonacci_khong_de_quy(n)
print(f"Số Fibonacci thứ {n} là {result}")

# Đệ quy
def fibonacci_de_quy(n):
    if n <= 1:
        return n
    else:
        return fibonacci_de_quy(n - 1) + fibonacci_de_quy(n - 2)
# Số Fibonacci thứ n bạn muốn tìm
n = 10  # Thay thế số này bằng số Fibonacci thứ n bạn muốn
result = fibonacci_de_quy(n)
print(f"Số Fibonacci thứ {n} là {result}")
'''
#6
'''
# Không đệ quy
def tong_fibonacci_khong_de_quy(n):
    if n <= 0:
        return 0
    a, b, total = 0, 1, 0
    for _ in range(n):
        total += a
        a, b = b, a + b
    return total

# Số lượng số Fibonacci bạn muốn tính tổng
n = 10  # Thay thế số này bằng số lượng số Fibonacci bạn muốn tính tổng

result = tong_fibonacci_khong_de_quy(n)
print(f"Tổng {n} số Fibonacci đầu tiên là {result}")

# Đệ quy
def tong_fibonacci_de_quy(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_de_quy(n - 1) + tong_fibonacci_de_quy(n - 1)

def fibonacci_de_quy(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_de_quy(n - 1) + fibonacci_de_quy(n - 2)

# Số lượng số Fibonacci bạn muốn tính tổng
n = 10  # Thay thế số này bằng số lượng số Fibonacci bạn muốn tính tổng

result = tong_fibonacci_de_quy(n)
print(f"Tổng {n} số Fibonacci đầu tiên là {result}")
'''
#7
'''
import math

def tinh_tong_can_bac_hai(n):
    tong = 0
    for i in range(1, n + 1):
        can_bac_hai = math.sqrt(i)
        tong += can_bac_hai
    return tong

# Số nguyên đầu tiên bạn muốn tính tổng căn bậc 2
n = 10  # Thay thế số này bằng số lượng số bạn muốn tính tổng căn bậc 2

result = tinh_tong_can_bac_hai(n)
print(f"Tổng căn bậc 2 của {n} số nguyên đầu tiên là {result}")
'''
#8
'''
import math

def giai_phuong_trinh_bac_2(a, b, c):
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return x1, x2
    elif delta == 0:
        x = -b / (2*a)
        return x,
    else:
        return None

a, b, c = 1, -3, 2
nghiem = giai_phuong_trinh_bac_2(a, b, c)

if nghiem:
    if len(nghiem) == 1:
        print(f"Nghiệm kép x = {nghiem[0]}")
    else:
        x1, x2 = nghiem
        print(f"Hai nghiệm phân biệt: x1 = {x1}, x2 = {x2}")
else:
    print("Không có nghiệm thực cho phương trình này")
'''
#9
'''
def tinh_giai_thua(n):
    giai_thua = 1
    for i in range(1, n + 1):
        giai_thua *= i
    return giai_thua

# Số nguyên dương n bạn muốn tính giai thừa
n = 5  # Thay thế số này bằng số bạn muốn tính giai thừa

ket_qua = tinh_giai_thua(n)
print(f"{n}! = {ket_qua}")
'''
#10
'''
def in_tam_giac_duoi(n):
    for i in range(1, n + 1):
        for j in range(i):
            print('*', end=' ')
        print()

# Số hàng (cột) bạn muốn in
n = 6  # Thay thế số này bằng số hàng (cột) bạn muốn

in_tam_giac_duoi(n)
'''
#11
'''
def doi_giay_thanh_thoi_gian(so_giay):
    gio = so_giay // 3600  # Số giờ (3600 giây trong 1 giờ)
    phut = (so_giay % 3600) // 60  # Số phút (60 giây trong 1 phút)
    giay = so_giay % 60  # Số giây

    return f"{gio}:{phut}:{giay}"

# Số giây bạn muốn đổi thành định dạng giờ:phút:giây
so_giay = 3770

thoi_gian = doi_giay_thanh_thoi_gian(so_giay)
print(thoi_gian)
'''
#12 côk


