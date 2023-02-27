from random import randint
from typing import Tuple

DESCRIPTION = 'What number is missing in the progression?'
PROGRESSION_LENGTH = 5


def generate_question_and_answer() -> Tuple[str, str]:
    hidden_index = randint(0, PROGRESSION_LENGTH - 1)
    step = randint(1, 10)

    start = randint(1, 100)
    progression = [start * i + step for i in range(PROGRESSION_LENGTH)]

    answer = str(progression[hidden_index])
    progression[hidden_index] = '..'
    question = ' '.join(map(str, progression))

    return question, answer
