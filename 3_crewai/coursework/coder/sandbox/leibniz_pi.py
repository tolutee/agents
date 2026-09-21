from decimal import Decimal, getcontext


def calculate_pi_like_series(terms: int = 1_000_000) -> Decimal:
    """Calculate 4 * (1 - 1/3 + 1/5 - 1/7 + ... ) for the given number of terms."""
    getcontext().prec = 50

    total = Decimal(0)
    sign = Decimal(1)

    for n in range(terms):
        denominator = 2 * n + 1
        total += sign / Decimal(denominator)
        sign = -sign

    return total * 4


if __name__ == "__main__":
    result = calculate_pi_like_series(1_000_000)
    print(result)
