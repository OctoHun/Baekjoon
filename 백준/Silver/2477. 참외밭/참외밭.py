k = int(input())
direction = [0] * 6
distance = [0] * 6
for i in range(6):
    direction[i], distance[i] = map(int, input().split())
max_row_distance = 0
max_col_distance = 0
for i in range(6):
    if direction[i] < 3 and distance[i] > max_row_distance:
        max_row_distance = distance[i]
        max_row_direction = direction[i]
        max_row_i = i
    elif direction[i] > 2 and distance[i] > max_col_distance:
        max_col_distance = distance[i]
        max_col_i = i
if (max_row_i+1)%6 == max_col_i:
    extra = distance[(max_row_i+3)%6] * distance[(max_row_i+4)%6]
else:
    extra = distance[(max_row_i+2)%6] * distance[(max_row_i+3)%6]
print(((max_row_distance * max_col_distance) - extra) * k)
