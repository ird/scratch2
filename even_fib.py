""" Project Euler #2 - sum of even fibonacci numbers
"""
def simple_solution(N):
    """
    simple method: iterate through the fibonacci numbers adding up the even ones.
    """
    total = 0
    for i in fib():
        if i % 2 == 0:
            total += i
        if i >= N:
            break
    return total


def formula_solution(N):
    """
    slightly less simple: use the formula S(n) = F(n+2)-1 / 2 to get the sum
    of the even fibonacci numbers.
    proof:
    S(n) = sum of the even fib numbers = F(n) + F(n-3) +...+F(1)
    F(n) = F(n-1) + F(n-2) = 2F(n-2) + F(n-3)
    F(n+2)  = 2F(n) + F(n-1)
            = 2F(n) + 2F(n-3) + F(n-4)
            ...
            = 2[F(n)+F(n-3)+...+F(1)] + F(0) = 2*S(n) + 1
    """
    r = largest_even_fib(N)
    return (next_fib(r['previous'], r['largest_even'], 2) - 1) // 2


def main():
    N = 1e18
    j = 1000 # run 1000 times to get accurate profiler times
    while j > 0:
        simple_solution(N)
        formula_solution(N)
    """
    results {python3 -m cProfile even_fib.py}:
    ncalls  tottime  percall  cumtime  percall  filename:lineno(function)
     1000    0.001    0.000    0.033    0.000   even_fib.py:16(formula_solution)
     1000    0.029    0.000    0.043    0.000   even_fib.py:3(simple_solution)

    ==> no real savings from being clever; still have to calculate the sequence, which
    is what takes the time
    """

def fib():
    """ generator which produces fibonacci numbers, starting from 1, 2"""
    a, b = 0, 1
    while True:
        yield a + b
        a, b = b, a + b


def next_fib(a, b, n):
    """ returns produces the nth fibonacci numbers following a, b"""
    while n > 0:
        a, b = b, a+b
        n = n - 1
    return b


def largest_even_fib(limit):
    """ given a limit, find the largest even fibonacci number below that limit,
    and the fibonacci number before it. Returned as a dict {'largest_even', 'previous'}"""
    results = {'largest_even': 0, 'previous': 0}
    largest = [0, 0, 0, 0]  # there is an even fib number every 3rd in the sequence
    a, b = 0, 1 # calculate the fib numbers inline rather than using a generator
    while True:
        i = a+b
        largest[3] = largest[2]
        largest[2] = largest[1]
        largest[1] = largest[0]
        largest[0] = i
        a, b = b, i
        if i >= limit:
            break
    for n in range(3):
        if largest[n] % 2 == 0:
            results['largest_even'] = largest[n]
            results['previous'] = largest[n+1]
            break
    return results

if __name__ == "__main__":
    main()
