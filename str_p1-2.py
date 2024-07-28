#1 ' '
#2 " "
#3 ''' '''
#4 """ """

# đều là chuỗi
strname = 'T"m nguyen'
print(strname)
# khác biệt '' và "" giống như dấu ngoặc vuông to hơn ngoặc đơn (đổi chức cho nhau được)

# 3,4 là chuỗi nhiều dòng
strmany = '''hpan
hpan
hpa'''
print(strmany)
# dùng \n để xuống dòng thay thế
'''
day la comment
'''
# dùng để comment được

#escape sequence (\) : đọc tài liệu 
print('\'')

# chuỗi trần (r) : dùng cho mở files
print(r'sua dc loi auto, \neu dung nhu nay')
# Nối chuỗi như bth (+)
# lặp lại n nguyên lần chuỗi (*)
print(strname*5)
# check ký tự 
strA = 'Nguyen'
strB = 'N'
# kí tự của strB có nằm trong strA hay không
strC = strB in strA
print(strC)
# Lấy kí tự
strD = strA[-1]
print(strD + '+' + str(type(strD)))
# lấy độ dài chuối len()
# lấy từ vị trí đâu đến đâu vd 1:5 /trái qua phải không tính vị trí 5
# nếu phải qua trái 1:5:2 /1 đến 5 với step là 2 , nếu mưốn phải qua trái dùng số âm
print(strA[::-1])

# ép kiểu như bth str() int() float()


 
