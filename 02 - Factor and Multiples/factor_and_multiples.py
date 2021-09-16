def display_options():
    print("1. Factor")
    print("2. Multiples")
    print("3. Quit")


def take_input():
    try:
        n = int(input("Enter the number: "))
        if n < 0:
            raise ValueError
        return n
    except ValueError:
        print("Please enter a positive integer")
        take_input()


def factor(num):
    for i in range(1, num + 1):
        if num % i == 0:
            print(i)


def multiples(num):
    limit = 20
    for i in range(1, limit+1):
        print(num * i)

def quit():
    print("Quit")


def main():
    display_options()
    choice = take_input()
    while choice != 3:
        if choice == 1:
            factor(take_input())
        elif choice == 2:
            multiples(take_input())
        else:
            print("Invalid choice")
        display_options()
        choice = take_input()
    quit()


if __name__ == "__main__":
    main()
