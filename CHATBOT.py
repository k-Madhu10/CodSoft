import random
import datetime

class Chatbot:
    def __init__(self, name):
        self.name = name
        self.responses = {
            "greeting": [
                "Hello !",
                "Hi, are you alright?",
                "Greetings! What can I do for you ?",
                "Nice to meet you! How can I help you?",
                "Hey there! What's on your mind?"
            ],
            "goodbye": [
                "Goodbye! Have a wonderful day!",
                "See you later! Take care.",
                "It was a pleasure talking with you. Goodbye!",
                "Until next time! Best wishes.",
                "Farewell! Take care."
            ],
            "time": [
                "The current time is: {}.",
                "It's {} right now.",
                "According to my clock, it's {}.",
                "The time is currently {}."
            ],
            "default": [
                "That's interesting. Tell me more!",
                "I'm not sure I understand. Can you rephrase?",
                "Hmm, I'm still learning. Let's try a another topic.",
                "That's a bit complex for me. Maybe try something else.",
                "I'm not able to answer that question."
            ]
        }

    def greet(self):
        return random.choice(self.responses["greeting"])

    def say_goodbye(self):
        return random.choice(self.responses["goodbye"])

    def get_time(self):
        now = datetime.datetime.now()
        formatted_time = now.strftime("%H:%M:%S")
        return random.choice(self.responses["time"]).format(formatted_time)

    def respond(self, message):
        # Basic keyword matching for time
        if "time" in message:
            return self.get_time()
        # Simple greetings and goodbyes
        elif "hii!" in message or "hi" in message:
            return self.greet()
        elif "bye!!" in message or "bye" in message:
            return self.say_goodbye()
        else:
            return random.choice(self.responses["default"])

    def start_conversation(self):
            print(f"Hello,I'm {self.name}!What can I do for you?")
            while True:
                user_input=input("You:")
                if user_input.lower()=="quit":
                    print(self.say_goodbye())
                    break
                else:
                    response=self.respond(user_input)
                    print(f"{self.name}:{response}")

my_chatbot=Chatbot("MADHU")               
my_chatbot.start_conversation()