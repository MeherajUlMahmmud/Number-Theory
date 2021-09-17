def take_input():
    print("Press q to exit")
    num = input("Enter a number: ")
    if num == 'q':
        print("Exiting...")
        exit()
    try:
        num = int(num)
        return num
    except ValueError:
        print("That was not a number")
        print("Try again")
        print()
        take_input()


def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)


def main():
    num = take_input()

    while True:
        print("Factorial of", num, "is", factorial(num))
        print()
        num = take_input()


if __name__ == '__main__':
    main()
