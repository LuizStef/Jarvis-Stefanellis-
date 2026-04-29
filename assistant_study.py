from base import Assistant

class AssistantStudy(Assistant):
    def __init__(self, subject):
        super().__init__("Study Assistant", "0.1")
        self.subject = subject

    def teach(self, topic):
        print(f"{self.name} is teaching about {topic}.")


    def evaluate(self, grade):
        print(f"{self.name} evaluated your answer with grade {grade}.")

        if grade >= 7:
            print("Approved!")
        else:
            print("Reprovado, continue estudando!")

assistente = AssistantStudy("Python")
assistente.introduce()
assistente.teach("OOP")
assistente.evaluate(8)