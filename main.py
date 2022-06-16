from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_bank.append(Question(question['text'], question['answer']))

quiz_brain_1 = QuizBrain(question_bank)

# print(vars(quiz_brain_1.current_question))
# 2:30

game_is_on = True
while game_is_on:
    question_number = quiz_brain_1.current_question_number
    question = quiz_brain_1.current_question.question
    user_input = input(f'Q.{question_number}: {question} (True/False)?: ')
    if user_input == 'quit':
        break
    elif user_input == 'restart':
        quiz_brain_1.restart()
    elif user_input.lower() == 'true':
        quiz_brain_1.move_to_next_question()
    elif user_input.lower() == 'false':
        quiz_brain_1.move_to_next_question()
    else:
        print('not a valid command')
