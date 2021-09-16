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


def sieve_of_eratosthenes(num):
    prime_list = []
    for i in range(2, num + 1):
        prime_list.append(i)

    for i in range(2, num // 2):
        for j in range(2, num // 2):
            if i * j <= num:
                print(i*j)
                prime_list[i * j - 2] = 0

    return prime_list


def print_list(list):
    for i in range(len(list)):
        if list[i] != 0:
            print(list[i], end=' ')
    print()


def main():
    num = take_input()

    while True:
        print("Prime numbers between 2 and {}:".format(num))
        print_list(sieve_of_eratosthenes(num))
        print()
        num = take_input()


if __name__ == '__main__':
    main()
