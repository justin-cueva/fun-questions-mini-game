class QuizBrain:
    def __init__(self, questions_list):
        self.questions_list = questions_list
        self.current_question_number = 1
        self.current_question = self.questions_list[self.current_question_number - 1]
        self.quiz_length = len(questions_list)

    def move_to_next_question(self):
        self.current_question_number += 1
        self.current_question = self.questions_list[self.current_question_number - 1]

    def restart(self):
        self.current_question_number = 1
        self.current_question = self.questions_list[self.current_question_number - 1]
