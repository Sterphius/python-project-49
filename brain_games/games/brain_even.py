from random import randint

DESCRIPTION = 'Answer \"yes\" if the number is even, otherwise answer \"no\".'


def generate_question_and_answer():
    random_number = randint(1, 100)
    question = str(random_number)

    expected_result = 'yes' if random_number % 2 == 0 else 'no'

    return question, expected_result
