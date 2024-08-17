from question_module import Question
from data import question_data
from quiz_brain import quizbrain


def ReturnBank():
    index = 0
    bank = []

    while index < len(question_data):
        ChosenDict = question_data[index]
        Text = None
        Answer = None
        for a, b in ChosenDict.items():

            if a.lower() == "text":
                Text = b
            elif a.lower() == "answer" and Text is not None:
                Answer = b
                question = Question(Text, Answer)
                bank.append(question)

        index += 1
    return bank


MyBank = ReturnBank()

Quiz = quizbrain(MyBank)

while Quiz.still_has_questions():
    Quiz.next_question()
