# CHAT BOT WITH RULED BASED RESPONSES :-
# Define a dictionary of predefined rules and responses
rules = {
    "hello": "Hello! How can I assist you today?",
    "how are you": "I'm just a chatbot, but I'm here to help!",
    "bye": "Goodbye! Have a great day!",
    "help": "Of course! How can I assist you?",
    "what's your name": "I'm just a chatbot, so I don't have a name, but you can call me ChatGPT.",
    "who created you": "I was created by a team of developers.",
    "what is the weather today": "I'm sorry, I can't provide real-time weather information. You can check a weather website or app.",
    "tell me a joke": "Sure! Why don't scientists trust atoms? Because they make up everything!",
    "what is the capital of France": "The capital of France is Paris.",
    "how old are you": "I'm just a computer program, so I don't have an age.",
    "what is the meaning of life": "The meaning of life is a philosophical question. Many believe it varies from person to person.",
    "tell me a fun fact": "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old!",
    "who won the World Series in 2021": "The Atlanta Braves won the World Series in 2021.",
    "what is the largest planet in our solar system": "Jupiter is the largest planet in our solar system.",
    "can you recommend a good book": "Certainly! I recommend 'To Kill a Mockingbird' by Harper Lee.",
    "what's the time": "I'm sorry, I can't provide the current time. You can check your device's clock.",
    "where is the Eiffel Tower located": "The Eiffel Tower is located in Paris, France.",
    "what's your favorite color": "I don't have preferences, but I can help you find information on colors!",
    "how do I bake a chocolate cake": "To bake a chocolate cake, you'll need ingredients like flour, cocoa, sugar, and a recipe. Would you like a recipe?",
    "what's the meaning of 'serendipity'": "Serendipity means finding something valuable or pleasant by chance or accident.",
    "tell me about space exploration": "Space exploration involves the discovery and exploration of outer space by means of space technology and space missions.",
    "what's the population of New York City": "The population of New York City is over 8 million people.",
    "what are the primary colors": "The primary colors are red, blue, and yellow.",
    "how do I learn to code": "Learning to code involves choosing a programming language, studying tutorials, and practicing by writing code.",
    "define 'sustainability'": "Sustainability is the practice of using resources in a way that preserves the environment and meets the needs of future generations.",
    "what is the Pythagorean theorem": "The Pythagorean theorem relates to the sides of a right triangle and is expressed as a² + b² = c².",
    "how can I improve my productivity": "To improve productivity, consider time management, setting goals, and minimizing distractions.",
    "tell me about the history of Rome": "Rome has a rich history dating back over 2,800 years, from its legendary founding to the Roman Empire.",
    "what is the Great Barrier Reef": "The Great Barrier Reef is the world's largest coral reef system, located in Australia.",
    "how does photosynthesis work": "Photosynthesis is the process by which plants convert sunlight, water, and carbon dioxide into energy and oxygen.",
    "define 'artificial intelligence'": "Artificial intelligence (AI) is the simulation of human intelligence in machines, enabling them to perform tasks that typically require human intelligence.",
    "how to stay healthy": "Staying healthy involves a balanced diet, regular exercise, and getting enough sleep.",
    "what is the Fibonacci sequence": "The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones (0, 1, 1, 2, 3, 5, 8, ...).",
    "what's your favorite movie": "I don't have favorites, but I can suggest some popular movies if you'd like!",
    "how does a car engine work": "A car engine works by burning fuel (usually gasoline) to create power, which moves the vehicle.",
    "what is the Hubble Space Telescope": "The Hubble Space Telescope is a space-based observatory that has provided stunning images and data about the universe.",
    "how to make a cup of tea": "To make tea, boil water, pour it over tea leaves or a tea bag, let it steep, and add any desired condiments (e.g., sugar, milk).",
    "tell me a riddle": "Sure! What comes once in a minute, twice in a moment, but never in a thousand years? Answer: The letter 'M'.",
    "what is the meaning of 'carpe diem'": "Carpe diem is a Latin phrase that means 'seize the day,' encouraging people to make the most of the present.",
    "how do I take care of houseplants": "Taking care of houseplants involves providing proper light, water, and occasional fertilization.",
    "what is the longest river in the world": "The Nile River is the longest river in the world.",
    "tell me about the history of the internet": "The internet's history dates back to the 1960s and has evolved into a global network of interconnected computers.",
    "what's the difference between 'their,' 'there,' and 'they're'": "Their, there, and they're are homophones but have different meanings and usages in English.",
    "how does a microwave work": "A microwave heats food by emitting microwave radiation that excites water molecules in the food, generating heat.",
    "tell me a famous quote": "Sure! 'The only way to do great work is to love what you do.' - Steve Jobs",
    "what's the largest desert in the world": "The largest desert in the world is the Antarctic Desert, followed by the Arctic Desert.",
    "how to make a paper airplane": "To make a paper airplane, fold a piece of paper in half, then fold the edges to create wings, and fold the wings down.",
    "tell me about the theory of relativity": "The theory of relativity, developed by Albert Einstein, describes the relationship between space, time, and gravity.",
    "what is renewable energy": "Renewable energy comes from sources that are naturally replenished, such as solar, wind, and hydroelectric power.",
    "what's the difference between 'affect' and 'effect'": "Affect is usually a verb, and effect is usually a noun. They have different meanings and usages.",
    "what is climate change": "Climate change refers to long-term shifts in global weather patterns, often associated with global warming."
}

# Function to process user input and generate a response
def chatbot_response(user_input):
    user_input = user_input.lower()  # Convert input to lowercase for case-insensitive matching

    # Check if the input matches any predefined rules
    if user_input in rules:
        return rules[user_input]
    else:
        return rules["default_response"]

# Main chat loop
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    response = chatbot_response(user_input)
    print("Chatbot:", response)
