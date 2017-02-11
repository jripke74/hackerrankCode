#!/bin/python3

import sys


n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t) 
diagonalLeftSum = 0
diagonalRightSum = 0

for j in range(n):
    for k in range(n):
        if j == k:
            diagonalLeftSum += a[j][k]
        if j + k == n - 1:
            diagonalRightSum += a[j][k]
difference = abs(diagonalLeftSum - diagonalRightSum)
print(difference)
