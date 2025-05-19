#!/usr/bin/env python3
# Created by: Adowk Adiebo
# Created on: May 18th, 2025
# This program calculates the area of a triangle.
def calc_area(base, height):
    #
    area = base * height / 2
    #
    print("The area of the triangle is: {}cm".format(area))


def main():
    # Ask the user for base as a string
    base_input = input("What is the base(cm): ")
    # Ask the user for height as a string
    height_input = input("What is the height(cm): ")

    try:
        # Convert the user base to an integer
        base_num = int(base_input)
        # Convert the user height to an integer
        height_num = int(height_input)

        if base_num <= 0 and height_num <= 0:
            # if base is less than 0 and height is less than 0
            # tell the user the base and height ust be positive.
            print("Your base and height must be positive numbers.")
        elif height_num <= 0:
            # if height is less than or equal to 0, tell the user the height must be a positive number.
            print(
                f"{height_num} must be a positive number\nThe height should always be positive."
            )
        elif base_num <= 0:
            # if base is less than or equal to 0, tell the user the base must be a positive number.
            print(
                f"{base_num} must be a positive number\nThe base should always be positive."
            )
        else:
            # Call the calc_area function if the user enters valid input.
            calc_area(base_num, height_num)

    except:
        # let the user know the input given is invalid
        print("This is an invalid number")

    finally:
        # Thank the user for participating
        print("Thank you for participating")


if __name__ == "__main__":
    main()
