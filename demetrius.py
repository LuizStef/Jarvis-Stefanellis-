from base import Assistant
from soul import Soul
from smart_memory import SmartMemory
from core import Core
from exceptions import InvalidMoodError, JarvisOfflineError
from semantic_memory import SemanticMemory

def log_action(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] {func.__name__} called")
        return func(*args, **kwargs)
    return wrapper

class Jarvis(Assistant):
    def __init__(self, username):
        super().__init__("Demetrius", "1.2")
        self.__mood = "neutral"
        self.soul = Soul(username, "casual")
        self.memory = SmartMemory()
        self.semantic = SemanticMemory()
        self.core = Core()

    def get_mood(self):
        return self.__mood

    def set_mood(self, value):
        if value in ["neutral", "excited", "tired"]:
            self.__mood = value
        else:
            raise InvalidMoodError(value)

    @log_action
    def respond(self, message):
        self.memory.save_memory("user", message)
        self.semantic.add(message)
        context = self.semantic.search(message)
        history = self.memory.load_history() 
        response = self.core.think(message, history)
        self.memory.save_memory("jarvis", response)
        print(f"[{self.name}]: {response}")

memory = SmartMemory()
username = memory.load_user()

if not username:
    username = input("Hello! What's your name? ")
    memory.save_user(username)

jarvis = Jarvis(username)
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
    
    elif message.lower() == "!clear":
        jarvis.memory.clear_history()
        print("[System]: Memory cleared.")
        
    elif message.lower() == "!history":
        for row in jarvis.memory.load_history():
            print(row)
            
    elif message.lower() == "!mood":
        print(f"[System]: Current mood: {jarvis.get_mood()}")
    
    elif message.lower() == "!stats":
        user_msgs = jarvis.memory.load_user_messages()
        jarvis_msgs = jarvis.memory.load_jarvis_messages()
        print(f"[System]: You sent {len(user_msgs)} messages.")
        print(f"[System]: Jarvis replied {len(jarvis_msgs)} times.")
     
    else:
        try:
             jarvis.respond(message)
        except JarvisOfflineError:
            print(f"[Jarvis]: I'm offline. Please start Ollama and try again.")
            