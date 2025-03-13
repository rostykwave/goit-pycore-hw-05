import re
from typing import Generator, Callable

def generator_numbers(text: str) -> Generator[float, None, None]:
    # match_pattern = r'\b\d+\.\d+\b'
    match_pattern = r'(?<=\s)(-?\d+(?:\.\d+)?)(?=\s)'
    # (?<=\s) – гарантує, що перед числом є пробіл.
    # -? – дозволяє від'ємні числа (-27.45).
    # \d+ – одне або більше цифр (1000 або 123).
    # (?:\.\d+)? – необов’язкова дробова частина (знаходить як 123.45, так і 1000).
    # (?=\s) – гарантує, що після числа є пробіл.

    for match in re.findall(match_pattern, text):
        yield float(match)


def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    return sum(func(text))


# Приклад використання
if __name__ == "__main__":
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")
    # Виведе: Загальний дохід: 1351.46
