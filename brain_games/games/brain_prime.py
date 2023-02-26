from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_question_and_answer():
    a = randint(1, 100)

    question = f'{a}'

    expected_result = 'yes' if is_prime_number(a) is True else 'no'

    return question, expected_result


def is_prime_number(value: int):
    if (value <= 0) or (value == 1) or (value % 2 == 0):
        return False

    for i in range(2, value // 2):
        if (value % i) == 0:
            return False

    return True
