from random import randint
from typing import Tuple

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_question_and_answer() -> Tuple[str, str]:
    random_number = randint(1, 100)
    question = str(random_number)

    answer = 'yes' if random_number % 2 == 0 else 'no'

    return question, answer
