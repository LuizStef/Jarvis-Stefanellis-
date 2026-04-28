from base import Assistant
from soul import Soul
from smart_memory import SmartMemory
from core import Core

class Jarvis(Assistant):
    def __init__(self, username):
        super().__init__("Jarvis", "0.1")
        self.__mood = "neutral"
        self.soul = Soul(username, "casual")
        self.memory = SmartMemory()
        self.core = Core()

    def get_mood(self):
        return self.__mood

    def set_mood(self, value):
        if value in ["neutral", "excited", "tired"]:
            self.__mood = value
        else:
            print("Invalid mood.")

    def respond(self, message):
        self.memory.save_memory("user", message)
        history = self.memory.load_history() 
        response = self.core.think(message, history)
        self.memory.save_memory("jarvis", response)
        print(f"[{self.name}]: {response}")



jarvis = Jarvis("User")
jarvis.soul.greet()
jarvis.introduce()

print("\n--- Memory ---")
for row in jarvis.memory.load_history():
    print(row)
print("---\n")

while True:
    message = input("You: ")
    if message.lower() == "exit":
        print(f"[{jarvis.name}]: Goodbye!")
        break
    jarvis.respond(message)
