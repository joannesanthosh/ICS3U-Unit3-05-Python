#!/usr/bin/env python3

# Created by: Joanne Santhosh
# Created on: Oct 2022
# This program outputs the month


def main():
    # this function checks the month

    # input
    grade_level = input("Enter month as a single number (ex: 1, 2, 3 ...): ")
    print("")

    # process & output
    match grade_level:
        case "1":
            print("January!")
        case "2":
            print("February!")
        case "3":
            print("March!")
        case "4":
            print("April!")
        case "5":
            print("May!")
        case "6":
            print("June!")
        case "7":
            print("July!")
        case "8":
            print("August!")
        case "9":
            print("September!")
        case "10":
            print("October!")
        case "11":
            print("November!")
        case "12":
            print("December!")
        case _:
            print("Invalid entry")

    print("\nDone.")


if __name__ == "__main__":
    main()
