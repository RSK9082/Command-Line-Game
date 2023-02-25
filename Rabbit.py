# python command line game of rabbit

import random
import keyboard
import time


def rabbit_game():

    gen = random.sample(range(0, 50), 3)
    arr = ["_"] * 47
    arr.insert(gen[0], "o")
    arr.insert(gen[1], "c")
    arr.insert(gen[2], "r")
    pointer = gen[2]   # this will point to the character 'r'

    print("\nControl : a --> left , b --> right , p --> pick , j --> jump")

    while True:
        print("", end="\r")
        for i in range(0, len(arr)):
            print(arr[i] if (pointer != i) else arr[pointer], end="")

        if keyboard.is_pressed("a") and pointer != len(arr) and arr[pointer-1] == "_":
            arr[pointer], arr[pointer - 1] = arr[pointer - 1], arr[pointer]
            pointer -= 1

        elif keyboard.is_pressed("a") and pointer != len(arr) and arr[pointer - 1] == "_" and arr[pointer] == "R":
            arr[pointer], arr[pointer - 1] = arr[pointer - 1], arr[pointer]
            pointer -= 1

        elif keyboard.is_pressed("d") and pointer != len(arr)-1 and arr[pointer+1] == "_":
            arr[pointer],arr[pointer + 1] = arr[pointer + 1], arr[pointer]
            pointer += 1

        elif keyboard.is_pressed("p") and pointer != len(arr)-1 and arr[pointer - 1] == "c":
            arr.remove('c')
            pointer -= 1
            arr[pointer] = "R"

        elif keyboard.is_pressed("p") and pointer != len(arr)-1 and arr[pointer+1] == "c":
            arr.remove("c")
            arr[pointer] = "R"

        elif keyboard.is_pressed("j") and pointer != len(arr)-1 and arr[pointer - 1] == "o" :
            arr[pointer], arr[pointer - 2] = arr[pointer - 2], arr[pointer]
            pointer -= 2

        elif keyboard.is_pressed("p") and pointer != len(arr)-1 and arr[pointer - 1] == "o" and arr[pointer] == "R":
            print("\nCongratulations you had completed the game ")
            break

        elif keyboard.is_pressed("p") and pointer != len(arr)-1 and arr[pointer + 1] == "o" and arr[pointer] == "R":
            print("\nCongratulations you had completed the game ")
            break

        elif keyboard.is_pressed("j") and pointer != len(arr)-1 and arr[pointer + 1] == "o" and arr[pointer] == "r":
            arr[pointer], arr[pointer + 2] = arr[pointer + 2], arr[pointer]
            pointer += 2

        elif keyboard.is_pressed("d") and arr[pointer] == "R" and pointer != len(arr)-1 and arr[pointer + 1] == "_":
            arr[pointer], arr[pointer + 1] = arr[pointer + 1], arr[pointer]
            pointer += 1

        elif keyboard.is_pressed("d") and arr[pointer] == "R" and pointer == len(arr)-1:
            arr[pointer] = arr[pointer]

        elif keyboard.is_pressed("d") and arr[pointer] == "r" and pointer == len(arr):
            arr[pointer] = arr[pointer]
            arr[pointer + 1] = arr[pointer + 1]

        time.sleep(0.1)


if __name__ == '__main__':

    rabbit_game()
    while True:
        b = input("Do you want to play again(y/n) : ")
        if b == "y":
            rabbit_game()
        else:
            break







