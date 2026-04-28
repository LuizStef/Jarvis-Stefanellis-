import ollama

class Core:
    def __init__(self):
        self.__model = "mistral"
        
    def think(self, message, history=[]):
        messages = []
        for role, content, _ in history:
            messages.append({"role": role, "content": content})
        messages.append({"role": "user", "content": message})
        
        response = ollama.chat(
            model=self.__model,
            messages=messages
        )
        
        return response["message"]["content"]
    
