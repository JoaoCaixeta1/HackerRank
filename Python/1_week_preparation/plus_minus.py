import math

def proportion():
    n = int(input())
    arr = list(map(int, input().split()))
    cont_pos = 0
    cont_neg = 0
    cont_zero = 0
    for i in arr:
        if i>0:
            cont_pos += 1
        if i<0:
            cont_neg += 1
        if i==0:
            cont_zero += 1
    pos = cont_pos/n
    neg = cont_neg/n
    zero = cont_zero/n
    print(f"{pos:.6f}")
    print(f"{neg:.6f}")
    print(f"{zero:.6f}")

proportion()  