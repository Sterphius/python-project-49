from random import randint
from typing import Tuple

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def generate_question_and_answer() -> Tuple[str, str]:
    num1, num2 = randint(1, 100), randint(1, 100)

    answer = str(find_gcd(num1, num2))
    question = f'{num1} {num2}'

    return question, answer


def find_gcd(num1: int, num2: int) -> int:

    exc = 'The gcd is undefined if at least one of value is equal to 0'
    if num1 == 0 or num2 == 0:
        raise Exception(exc)

    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1

    return max(num1, num2)
