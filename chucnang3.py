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