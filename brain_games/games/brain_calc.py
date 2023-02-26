import operator
from random import randint, choice

DESCRIPTION = 'What is the result of the expression?'


def generate_question_and_answer():
    num1, num2 = randint(1, 100), randint(1, 100)

    operations = ('+', '-', '*')
    operation = choice(operations)

    question = f'{num1} {operation} {num2}'

    expected_result = str(expected_result_from(num1, num2, operation))

    return question, expected_result


def expected_result_from(a: int, b: int, op: str):

    operation_result = {
        '+': operator.add(a, b),
        '-': operator.sub(a, b),
        '*': operator.mul(a, b)
    }

    return operation_result[op]
