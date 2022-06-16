class QuizBrain:
    def __init__(self, questions_list):
        self.questions_list = questions_list
        self.current_question_number = 1
        self.current_question = self.questions_list[self.current_question_number - 1]
        self.quiz_length = len(questions_list)
        self.game_is_on = True
        self.score = 0

    def check_answer(self, users_answer, correct_answer):
        answered_correct = users_answer.lower() == correct_answer.lower()
        if answered_correct:
            self.score += 1
        print(f'You got it {"RIGHT" if answered_correct else "WRONG"}!')
        print(f'The correct answer was: {correct_answer}.')
        print(f'Your current score is: {self.score}/{self.current_question_number}.')
        print('\n')
        if self.current_question_number == self.quiz_length:
            self.game_is_on = False

    def move_to_next_question(self, users_answer):
        self.check_answer(users_answer, self.current_question.answer)
        if not self.game_is_on:
            return
        self.current_question_number += 1
        self.current_question = self.questions_list[self.current_question_number - 1]

    def terminate(self):
        self.game_is_on = False

    def restart(self):
        self.score = 0
        self.current_question_number = 1
        self.current_question = self.questions_list[self.current_question_number - 1]
