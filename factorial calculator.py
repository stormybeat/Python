import sys
sys.set_int_max_str_digits(0)
num = int(input())
file = open(f'./factorials/{num}_factorial.txt', 'w')
answer = num
while num > 1:
    answer = answer * (num-1)
    num -= 1
else:
    file.write(str(answer))
file.close()
