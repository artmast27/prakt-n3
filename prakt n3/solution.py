#!/usr/bin/env python3
# solution.py
# Рішення для задачі:
# Кількість чисел з r розрядів, використовуючи цифри 5 та 9, без трьох однакових підряд.

def count_no_three(r: int) -> int:
    if r <= 0:
        return 0
    A = [0]*(r+1)
    B = [0]*(r+1)
    A[1] = 2
    B[1] = 0
    for n in range(2, r+1):
        A[n] = A[n-1] + B[n-1]
        B[n] = A[n-1]
    return A[r] + B[r]

def main():
    try:
        r = int(input("Введи r (1..30): "))
    except ValueError:
        print("invalid input")
        return
    if r > 30 or r < 1:
        print("r out of range (1..30)")
        return
    print("Кількість чисел:", count_no_three(r))
    input("Натисни Enter для виходу...")

if __name__ == "__main__":
    main()
