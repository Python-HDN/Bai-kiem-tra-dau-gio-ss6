def main ():
    # Chức năng 1: Nhập số lượng tồn kho
    stock = int (input ("Nhập số lượng tồn kho: "))
    if stock >= 50: 
        print ("Tình trạng: Hàng đầy kho.")
    elif stock >= 10 and stock < 50:
        print ("Tình trạng: Mức an toàn.")
    elif stock < 10 and stock >= 0:
        print ("Tình trạng: Sắp hết hàng, cần báo cáo nhập thêm.")
    elif stock < 0:
        print ("Số lượng nhập vào không hợp lệ.")
    # Chức năng 2: Nhập số lượng hàng lỗi
    total_error_goods = 0
    while True:
        error_goods = int(input ("Nhập số lượng hàng lỗi: "))
        if (error_goods == -1):
            break
        else:
            total_error_goods = total_error_goods + error_goods
    print (f"Tổng số hàng lỗi là: {total_error_goods}")
    # Chức năng 3: Nhập số lượng xuất kho
    inventory = 100
    while True: 
        qty = int (input("Nhập số lượng muốn xuất: "))
        if qty < 0:
            print ("Số lượng muốn xuất không hợp lệ")
        elif qty > inventory:
            print ("Số lượng tồn kho không đủ để xuất")
        else:
            inventory = inventory - qty
            print ("Xuất kho thành công.")
            print ("Còn lại {}".format(inventory))
            break
            
if __name__ == "__main__":
    main()