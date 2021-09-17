import math


def take_input():
    display_options()
    choice = input("Enter your choice: ")
    if choice == '1':
        num = int(input("Enter the number of terms: "))
        fibonacci(num)
    elif choice == '2':
        num = int(input("Enter the number of terms: "))
        fibonaci_using_golden_ratio(num)
    elif choice == '3':
        exit()
    else:
        print("Invalid choice")
        return take_input()


def display_options():
    print("1. Fibonacci Sequence")
    print("2. Fibonacci Sequence using Golden Ratio")
    print("3. Exit")
    print()


def fibonacci(num):
    seq = []
    seq.append(0)
    seq.append(1)

    for i in range(2, num + 1):
        seq.append(seq[i - 1] + seq[i - 2])
    print("Fibonacci Sequence")
    print(seq)


def fibonaci_using_golden_ratio(num):
    seq = []
    seq.append(0.0)
    seq.append(1.0)
    seq.append(1.0)

    rounded_seq = []
    rounded_seq.append(0.0)
    rounded_seq.append(1.0)
    rounded_seq.append(1.0)

    golden_ratio = round((1 + 5 ** 0.5) / 2, 6)
    print("Golden Ratio: ", golden_ratio)
    for i in range(3, num + 1):
        seq.append((golden_ratio ** i - (1 - golden_ratio) ** i) / (5 ** 0.5))
        rounded_seq.append(
            round((golden_ratio ** i - (1 - golden_ratio) ** i) / (5 ** 0.5), 0))
    print("Fibonacci Sequence")
    print("Actual Sequence:", seq)
    print("Rounded Sequence:", rounded_seq)


def main():
    while True:
        take_input()
        print()


if __name__ == '__main__':
    main()
