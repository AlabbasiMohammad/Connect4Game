#initialisation script
#Store y coordinates in col_x
x_coord = -600
y_coord = -481
col_x = []
row_y = []
#column =0
for column in range(7):
    #col_x.append(x_coord)
    col_x.insert(column, x_coord)
    x_coord += 150
    column += 1
print(col_x)
#Store x coordinates in col_y
for row in range(7):
    row_y.insert(row, y_coord)
    y_coord += 151
    row += 1
print(row_y)
col_1 = []
col_2 = []
col_3 = []
col_4 = []
col_5 = []
col_6 = []
col_7 = []
for i in range(6):
    col_1.append(0)
    col_2.append(0)
    col_3.append(0)
    col_4.append(0)
    col_5.append(0)
    col_6.append(0)
    col_7.append(0)
    i += 1
print(col_1)
print(col_2)
print(col_3)
print(col_4)
print(col_5)
print(col_6)
print(col_7)









#check for win script

_test_row = [0, 0, 0, 0, 0, 0, 0] #7

#when you receive ... check for win
#tests_complete = False
#turn = 0
#if turn >= 7 :
#    test_horizontals()
#
#
#
#def test_horizontals():
#    _idx =0
#    for _idx in range(6):
#        _test_row = [_idx] = item []
#
#




