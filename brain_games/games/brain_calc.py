import operator
from random import randint, choice
from typing import Tuple

DESCRIPTION = 'What is the result of the expression?'


def generate_question_and_answer() -> Tuple[str, str]:
    rnd_num1, rnd_num2 = randint(1, 100), randint(1, 100)

    operations = ('+', '-', '*')
    operation = choice(operations)

    question = f'{rnd_num1} {operation} {rnd_num2}'

    answer = str(get_formatted_result(rnd_num1, rnd_num2, operation))

    return question, answer


def get_formatted_result(a: int, b: int, op: str) -> str:

    operation_result = {
        '+': operator.add(a, b),
        '-': operator.sub(a, b),
        '*': operator.mul(a, b)
    }

    return operation_result[op]
