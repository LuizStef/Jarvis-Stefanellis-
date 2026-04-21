class Soul:
    def __init__(self, name, style):
        self.__username = name
        self.__style = style

    def get_username(self):
        return self.__username

    def set_username(self, value):
        self._username = value

    def get_style(self):
        return self.__style
    
    def set_style(self, value):
        if value in ["formal", "casual", "technical"]:
            self.__style = value
        else:
            print("Style inválido.")

    def greet(self):
        if self.__style == "formal":
            print(f"Hello, {self.__username}. How can I help you?")
        elif self.__style == "casual":
            print(f"Hey, {self.__username}! How can I assist you?")
        elif self.__style == "technical":
            print(f"Hello, {self.__username}. Waiting for command.")


soul = Soul("User", "formal")
soul.greet()
soul.set_style("casual")
soul.greet()
soul.set_style("Happy")  # Invalid style for testing
