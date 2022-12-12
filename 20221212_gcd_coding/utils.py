import numpy


def get_divisors(n: int):
    assert 1 <= n and isinstance(n, int)
    range_max = int(numpy.sqrt(abs(n)))
    pair_list = [(i, n / i) for i in range(1, range_max + 1) if n % i == 0]
    return sum(pair_list, [])
