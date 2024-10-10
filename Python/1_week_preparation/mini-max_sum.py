import math

def miniMaxSum(arr):
    lista = (sorted(arr, reverse=False))
    min = sum(lista[:4])
    max = sum(lista[-4:]) 
    print(min, max)

arr = list(map(int, input().split()))
miniMaxSum(arr)