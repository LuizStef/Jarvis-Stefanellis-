import ollama
from datetime import datetime
from exceptions import JarvisOfflineError

class Core:
    def __init__(self):
        self.__model = "mistral"
        today = datetime.now().strftime("%d/%m/%Y %H:%M")
        self.__system_prompt = f"""You are Demetrius, a personal AI assistant created by Stefanelli
        You are helpful, intelligent and slighty informal
        Today time is {today}
        You remember previous conversations and learn from them
        Always respond concisely and directly."""
        
    def think(self, message, history=[], context=[]):
        messages = [{"role": "system", "content": self.__system_prompt}]
        
        if context:
            context_text = "\n".join(context)
            messages.append({
                "role": "system",
                "content": f"Relevant context from memory:\n{context_text}"
            })
        
        for role, content, _ in history:
            messages.append({"role": role, "content": content})
        messages.append({"role": "user", "content": message})

        try:
            response = ollama.chat(model=self.__model, messages=messages)
            return response["message"]["content"]
        except Exception as e:
            raise JarvisOfflineError() from e
    