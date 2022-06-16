from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_bank.append(Question(question['text'], question['answer']))

quiz_brain_1 = QuizBrain(question_bank)

# print('You got it right!')
# print('The correct answer was: True.')
# print('Your current score is: 1/1.')

while quiz_brain_1.game_is_on:
    question_number = quiz_brain_1.current_question_number
    question = quiz_brain_1.current_question.question
    user_input = input(f'Q.{question_number}: {question} (True/False)?: ')
    if user_input == 'quit':
        quiz_brain_1.terminate()
    elif user_input == 'restart':
        quiz_brain_1.restart()
    elif user_input.lower() == 'true' or user_input.lower() == 'false':
        quiz_brain_1.move_to_next_question(user_input)
    else:
        print('not a valid command')
