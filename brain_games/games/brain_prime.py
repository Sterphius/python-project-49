from random import randint
from typing import Tuple

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_question_and_answer() -> Tuple[str, str]:
    rand_int = randint(1, 100)

    question = f'{rand_int}'

    answer = 'yes' if is_prime_number(rand_int) is True else 'no'

    return question, answer


def is_prime_number(value: int) -> bool:
    if value < 2:
        return False

    for i in range(2, value // 2):
        if value % i == 0:
            return False

    return True
