from base import Assistant
from soul import Soul

class Jarvis(Assistant):
    def __init__(self, username):
        super().__init__("Jarvis", "0.1")
        self.__mood = "neutral"
        self.soul = Soul(username, "casual")

    def get_mood(self):
        return self.__mood

    def set_mood(self, value):
        if value in ["neutral", "excited", "tired"]:
            self.__mood = value
        else:
            print("Invalid mood.")

    def respond(self, message):
        print(f"[{self.name}]: I don't know the answer to that yet.")

jarvis = Jarvis("User")
jarvis.soul.greet()
jarvis.introduce()

while True:
    message = input("You: ")
    if message.lower() == "exit":
        print(f"[{jarvis.name}]: Goodbye!")
        break
    jarvis.respond(message)
