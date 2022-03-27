#!/usr/bin/env python3

# Created by: Dahrio Francois
# Created on: March 2022
# This program lets you know if the integer you inputted
# was positive, negative or just a 0
#   with user input


def main():
    # this program will state what kind of number it is

    integer = int(input("Input your number: "))

    # process
    if integer < 0:
        print("This number is negative!")
        print("\nDone")

    elif integer > 0:
        print("This number is positive!")
        print("\nDone")

    elif integer == 0:
        print("This number is a zero!")
        print("\nDone")


if __name__ == "__main__":
    main()
