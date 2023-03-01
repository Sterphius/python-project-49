import types

import prompt

from brain_games import cli

MAX_ROUNDS_COUNT = 3


def run(game: types.ModuleType) -> None:
    user_name = cli.welcome_user()

    print(game.DESCRIPTION)

    for _ in range(MAX_ROUNDS_COUNT):
        question, expected_answer = game.generate_question_and_answer()
        print(f'Question: {question}')

        actual_answer = prompt.string('Your answer: ')
        result = actual_answer.lower() == expected_answer

        wrong_msg = f"\'{actual_answer}\' is wrong answer ;(. " \
            f"Correct answer was \'{expected_answer}\'.\n "\
            f"Let\'s try again, {user_name}!"

        if not result:
            print(wrong_msg)
            return
        print('Correct')

    print(f'Congratulations, {user_name}!')
