tri_height = 4
max_level = tri_height + (tri_height - 1)
for x in range(1, tri_height+1):
    if(x == 1):
        print(' ' * (max_level-x) + "*")
    else:
        print(' ' * (max_level-x) + '*' * (x + x-1))
