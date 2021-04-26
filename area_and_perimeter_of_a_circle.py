#!/usr/bin/env python3

# Created by: Ntare Katarebe
# Created on: April 2021
# This program calculates the area and perimeter of a circle
#     with radius 15mm

import math


def main():
    # this function calculates the area and perimeter

    print("If a circle has radius of 15mm:")
    print("")
    print('Area is {} mm^2.'.format(math.pi * 15 ** 2))
    print("Perimeter is {} mm.".format(2 * math.pi * 15))
    print("")
    print("Done")


if __name__ == "__main__":
    main()
