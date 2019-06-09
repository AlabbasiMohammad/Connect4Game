
board_ready = False
turn = 0
active_player = 1
active_column = 1
winner = False
_idx = 0


x_coord=[]
x = -355
i = 0
for i in range(8):
    x_coord.insert(i,x)
    x+=101.5
print(x_coord)
t = -304.25
x_c = []

for j in range(8):
    x_c.insert(j, t)
    t += 101.5
print(x_c)
