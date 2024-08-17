class quizbrain:
    def __init__(self, questions_list):
        self.QuestionNumber = 0
        self.QuestionsList = questions_list
        self.score = 0

    def next_question(self):
        current_question = self.QuestionsList[self.QuestionNumber]
        self.QuestionNumber += 1

        Choice = str(input(f"Q.{self.QuestionNumber}: {current_question} (True/False): \n"))
        self.check_answer(Choice, current_question.Answer)

    def still_has_questions(self):
        return self.QuestionNumber < len(self.QuestionsList)

    def check_answer(self, UserAnswer, CorrectAnswer):
        if UserAnswer.lower() == str(CorrectAnswer).lower():
            self.score += 1
            print(f"You are correct!")
        else:
            print(f"You guessed wrong, the correct answer was {CorrectAnswer}.")

        print(f"Your current score is: {self.score}/{self.QuestionNumber}.\n")
