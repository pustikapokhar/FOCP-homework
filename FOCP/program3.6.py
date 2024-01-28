'''Write a program that displays the "Seven Times Table". That is, the result of
multiplying 7 by every number from 0 to 12 inclusive. The output might start:
0 x 7 = 0
1 x 7 = 7
2 x 7 = 14
and so on'''
def main():
    print("The table of 7 is:", table())


def table():
    for x in range(0, 13):
        print(f"{x} x 7 = {x * 7}")


main()
