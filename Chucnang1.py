stock = int (input ("Nhập số lượng tồn kho: "))
if stock >= 50: 
    print ("Tình trạng: Hàng đầy kho.")
elif stock >= 10 and stock < 50:
    print ("Tình trạng: Mức an toàn.")
elif stock < 10 and stock >= 0:
    print ("Tình trạng: Sắp hết hàng, cần báo cáo nhập thêm.")
elif stock < 0:
    print ("Số lượng nhập vào không hợp lệ.")