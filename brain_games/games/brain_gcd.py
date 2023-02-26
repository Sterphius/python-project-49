from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def generate_question_and_answer():
    num1, num2 = randint(1, 100), randint(1, 100)

    expected_result = str(find_gcd_from_values(num1, num2))
    question = f'{num1} {num2}'

    return question, expected_result


def find_gcd_from_values(num1: int, num2: int):
    if (num1 < 1) or (num2 < 1):
        raise Exception('The gcd of values lower than 1 is undefined')

    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1

    return max(num1, num2)
