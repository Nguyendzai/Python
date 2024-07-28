a = 'My name is %s%suyen'
print(a %('n','g'))
# thay thế vào lần lượt %s 
# còn có %r %d %f
f = '%.3f' %(3.999999)
print(f)

# chuỗi f
name = 'nguyen'
hvt = f'ho pham anh {name}{{khong}}'
print(hvt)

# format
format = 'a:{}, b:{}, c:{}'.format(1,2,3)
print(format)
# sắp xếp
format_1 = 'a:{1}, b:{0}, c:{2}'.format(1,2,3)
print(format_1)
# gán
format_2 = 'a:{one}, b:{two}, c:{three}'.format(one=1,two=2,three=3)
print(format_2)
# căn lề
# 1_lề trái: {:(c)<n} 2_lề phải: {:(c)>n} 3_giữa {:(c)^n}
# n là số kí tự (c)
can = '{:_^13}'.format('1b1')
print(can)

# ứng dụng tạo bảng

# phần định dạng
row_1 = '+ {:-<6} + {:-^15} + {:->10} +'.format('', '', '')
row_2 = '| {:<6} | {:^15} | {:>10} |'.format('ID', 'Ho va ten', 'Noi sinh')
row_3 = '| {:<6} | {:^15} | {:>10} |'.format('123', 'Kpan', 'HA TINH')
row_4 = '| {:<6} | {:^15} | {:>10} |'.format('6969', 'Hpan', 'HA NOI')
row_5 = '+ {:-<6} + {:-^15} + {:->10} +'.format('', '', '')
# phần xuất kết quả
print(row_1)
print(row_2)
print(row_3)
print(row_4)
print(row_5)

print('\nnguyen dep trai')
# testttt
