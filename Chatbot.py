import random

responses = {
    "hello": ["Hello!", "Hi there!", "Greetings!"],
    "how are you?": ["I'm good, thank you!", "I'm doing great!", "All is well!"],
    "bye": ["Goodbye!", "Farewell!", "Take care!"],
    "default": ["Sorry, I didn't understand.", "Could you please rephrase that?", "I'm still learning!"],
}

def get_response(message):
    message = message.lower()

    if message in responses:
        return random.choice(responses[message])
    else:
        return random.choice(responses["default"])

while True:
    user_input = input("Mayur: ")

    bot_response = get_response(user_input)

    print("ChatBot:", bot_response)

    if user_input.lower() == "bye":
        break
