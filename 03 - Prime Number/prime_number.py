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


def is_prime(num):
    if num > 1:
        for i in range(2, num//2):
            if (num % i) == 0:
                print(num, "is not a prime number")
                print(i, "times", num // i, "is", num)
                print()
                break
        else:
            print(num, "is a prime number")
            print()
    else:
        print(num, "is not a prime number")
        print()


def main():
    num = take_input()

    while True:
        is_prime(num)
        num = take_input()


if __name__ == "__main__":
    main()
