from functools import lru_cache


@lru_cache(maxsize=64)
def fib(number: int) -> int:
    if number == 0 or number == 1:
        return number
    if number > 1:
        number = fib(number - 1) + fib(number - 2)
    return number


def update_fib_number_assinc(fibonacci_number):
    fibonacci_number.fib_number = fib(
        fibonacci_number.original_number
    )
    fibonacci_number.save()
