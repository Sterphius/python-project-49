from random import randint

DESCRIPTION = 'What number is missing in the progression?'
PROGRESSION_LENGTH = 5


def generate_question_and_answer():
    k = randint(0, PROGRESSION_LENGTH-1)
    diff = randint(1, 10)

    array = [randint(1, 100)]

    for i in range(1, PROGRESSION_LENGTH):
        array.append(array[i - 1] + diff)

    expected_result = str(array[k])
    array[k] = '..'
    question = ' '.join(map(str, array))

    return question, expected_result
