total_error_goods = 0
while True:
    error_goods = int(input ("Nhập số lượng hàng lỗi: "))
    if (error_goods == -1):
        break
    else:
        total_error_goods = total_error_goods + error_goods
print (f"Tổng số hàng lỗi là: {total_error_goods}")