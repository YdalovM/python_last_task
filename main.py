num = int(input())
ti_pidor = 0
for i in range(2, num):
    if num % i == 0:
        ti_pidor += 1
if ti_pidor > 0:
    print('Число', num, 'не простое')
else:
    print('Число', num, 'простое')
