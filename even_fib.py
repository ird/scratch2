""" Project Euler #2 - sum of even fibonacci numbers
"""
def fib():
    """ generator which produces fibonacci numbers, starting from 1, 2"""
    a, b = 0, 1
    while True:
        yield a + b
        a, b = b, a + b


def main():
    total = 0
    evens = 0
    odds = 0
    for i in fib():
        if i % 2 == 0:
            total += i
            evens += 1
        else:
            odds += 1
        if i >= 4e6:
            break

    print("There are", evens, "even fibonacci numbers < 4e6. They add up to", total)
    print("Odd fib numbers:", odds)


if __name__ == "__main__":
    main()
