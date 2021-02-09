a = int(input())
import time

if 1000 <= a <= 9999 and (a % 7) == 0 and (a % 17) == 0:
    print('YES')
else:
    print('NO')
    print(a%7)
    print(a%17)
    time.sleep(12)