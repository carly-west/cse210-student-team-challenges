

class Welcome:
    def __init__(self):
        self.user_prompt = "What is your name? "

    def welcome_user(self):
        print()
        print("------------------------")
        print("Welcome to Jumper!")
        print()
        user_name = input(self.user_prompt)
        print()
        return user_name
