from math import isqrt
from random import randint
from typing import Tuple

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_question_and_answer() -> Tuple[str, str]:
    rnd_num = randint(1, 100)

    question = f'{rnd_num}'

    answer = 'yes' if is_prime_number(rnd_num) is True else 'no'

    return question, answer


def is_prime_number(value: int) -> bool:
    if value < 2:
        return False

    for i in range(2, isqrt(value) + 1):
        if value % i == 0:
            return False

    return True
