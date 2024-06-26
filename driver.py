"""
Author: Charlie Doherty
KUID: 3115329
Date: 4/10/24
Lab: 08
Last modified: 4/10/24
Purpose: Utilize a Max Heap to simulate a hospital with a priority queue

Run Driver.py to begin the program
"""

from hospital import Hospital

if __name__ == "__main__":

    # Runs until a valid file input is given
    while True:

        try:
            file_name = input("Enter the name of the input file: ")
            my_exec = Hospital(file_name)
            my_exec.run()
            break

        except FileNotFoundError:
            print("\nNot a valid file.\n")
