def take_input():
    length = int(input("How many numbers? "))
    numbers = []
    for i in range(length):
        numbers.append(int(input("Enter number: ")))
    print("Numbers:", numbers)
    return numbers


def gcd_2(a, b):
    if b == 0:
        return a
    else:
        return gcd_2(b, a % b)


def gcd(numbers):
    if len(numbers) == 1:
        return numbers[0]

    ans = 1
    for i in range(1, len(numbers)):
        if i == 1:
            ans = gcd_2(numbers[0], numbers[1])
        ans = gcd_2(ans, numbers[i])
    return ans


def main():
    numbers = take_input()

    while True:
        print("Greatest Common Divisor", gcd(numbers))
        print()
        numbers = take_input()


if __name__ == '__main__':
    main()
