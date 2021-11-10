class Quiz:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

prompt = [
    "What is CPU stands for? = ",
    "When Bangladesh was independent? = ",
    "What color are Strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n= "
]

questions = [
    Quiz(prompt[0], "Central Processing Unit"),
    Quiz(prompt[1], "1971"),
    Quiz(prompt[2], "b")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)