from random import randint
from typing import Tuple

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_question_and_answer() -> Tuple[str, str]:
    rnd_num = randint(1, 100)
    question = str(rnd_num)

    answer = 'yes' if rnd_num % 2 == 0 else 'no'

    return question, answer
