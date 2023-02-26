import types

import prompt

from brain_games import cli

MAX_ROUNDS_COUNT = 3
BRAIN_GAMES_MODULE_NAME = 'brain_games.games.brain_games'


def run(game: types.ModuleType = None):
    user_name = cli.welcome_user()

    if game is not None:
        '''This check is for the game: brain_games
        where the game step is welcoming user only'''
        if game.__name__ != BRAIN_GAMES_MODULE_NAME:
            print(game.DESCRIPTION)
        else:
            return
    else:
        raise TypeError

    for _ in range(0, MAX_ROUNDS_COUNT):
        question_str, expected_answer = game.generate_question_and_answer()
        print(f'Question: {question_str}')

        actual_answer = prompt.string('Your answer: ')
        result = True if actual_answer.lower() == expected_answer else False

        wrong_msg = f"\'{actual_answer}\' is wrong answer ;(. " \
            f"Correct answer was \'{expected_answer}\'.\n "\
            f"Let\'s try again, {user_name}!"

        if not result:
            print(wrong_msg)
            return
        print('Correct')

    print(f'Congratulations, {user_name}!')
