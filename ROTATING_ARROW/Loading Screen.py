import os
import time
import sys

print("\n")
# time.sleep(2)
spaces_1 = 40
astrics_1 = 1
while True:
    if astrics_1 > 10:
        break
    for i in range(0, spaces_1):
        print(" ", end="")
    for j in range(0, astrics_1):
        print("*", end="")
    print("")
    astrics_1 += 1

time.sleep(1)

print("\033[11A")


spaces_2 = 38
astrics_2 = 1
while True:
    if astrics_2 > 10:
        break
    for i in range(0, spaces_2):
        print(" ", end="")
    for j in range(0, astrics_2):
        print("*", end="")
    print("")
    spaces_2 -= 1
    astrics_2 += 1

time.sleep(1)

spaces_3 = 28
astrics_3 = 1
while True:
    if astrics_3 > 10:
        break
    for i in range(0, spaces_3):
        print(" ", end="")
    for j in range(0, astrics_3):
        print("*", end="")
    print("")
    spaces_3 -= 1
    astrics_3 += 1

time.sleep(1)

spaces_4 = 19
astrics_4 = 10
while True:
    if astrics_4 < 1:
        break
    for i in range(0, spaces_4):
        print(" ", end="")
    for j in range(0, astrics_4):
        print("*", end="")
    print("")
    spaces_4 += 1
    astrics_4 -= 1

time.sleep(1)

spaces_5 = 29
astrics_5 = 10
while True:
    if astrics_5 < 1:
        break
    for i in range(0, spaces_5):
        print(" ", end="")
    for j in range(0, astrics_5):
        print("*", end="")
    print("")
    spaces_5 += 1
    astrics_5 -= 1

time.sleep(1)

print("\033[10A", end="")

astrics_6 = 10
while True:
    if astrics_6 < 1:
        break

    print("\033[40C", end="")

    for j in range(0, astrics_6):
        print("*", end="")
    print("")
    astrics_6 -= 1

time.sleep(1)

print("\033[20A", end="")

astrics_7 = 10
while True:
    if astrics_7 < 1:
        break

    print("\033[50C", end="")

    for j in range(0, astrics_7):
        print("*", end="")
    print("")
    astrics_7 -= 1

time.sleep(1)

print("\033[20A", end="")

astrics_8 = 1
while True:
    if astrics_8 > 10:
        break

    print("\033[50C", end="")

    for j in range(0, astrics_8):
        print("*", end="")
    print("")
    astrics_8 += 1

print("\033[33C", end="\033[1A")
time.sleep(1)


while 1:
    print("__ " * 5)

    time.sleep(0.3)

    print("\033[33C", end="\033[1A")
    print(" " * 14)



    print("\033[5A", end="")

    for i in range(8):
        print("\033[35C", end="")
        print(" " * i, end="")
        print("\\")

    time.sleep(0.3)

    print("\033[8A", end="")

    for i in range(8):
        print("\033[35C", end="")
        print(" " * i, end="")
        print(" ")


    print("\033[9A")
    for i in range(9):
        print("\033[39C", end="")
        print("|")

    time.sleep(0.3)

    print("\033[10A")
    for i in range(9):
        print("\033[39C", end="")
        print(" ")



    print("\033[8A", end="")

    for i in range(8, 0, -1):
        print("\033[35C", end="")
        print(" " * i, end="")
        print("/")

    time.sleep(0.3)

    print("\033[8A", end="")

    for i in range(8, 0, -1):
        print("\033[35C", end="")
        print(" " * i, end="")
        print(" ")

    print("\033[33C", end="\033[5A")
