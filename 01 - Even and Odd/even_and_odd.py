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


def even_or_odd(num):
    if num % 2 == 0:
        print(num, "is even")
        print()
    else:
        print(num, "is odd")
        print()


def main():
    num = take_input()
    while True:
        even_or_odd(num)
        num = take_input()


if __name__ == "__main__":
    main()
