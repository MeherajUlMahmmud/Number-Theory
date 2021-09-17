def take_input():
    length = int(input("How many numbers? "))
    numbers = []
    for i in range(length):
        numbers.append(int(input("Enter number: ")))
    print("Numbers:", numbers)
    return numbers


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


#  Find LCM of a list of numbers using division method
def lcm(numbers):
    if len(numbers) == 1:
        return numbers[0]
    elif len(numbers) == 2:
        return (numbers[0] * numbers[1]) // gcd(numbers[0], numbers[1])
    else:
        return (numbers[0] * lcm(numbers[1:])) // gcd(numbers[0], lcm(numbers[1:]))


def main():
    numbers = take_input()

    while True:
        print("Least Common Multiple", lcm(numbers))
        print()
        numbers = take_input()


if __name__ == '__main__':
    main()
