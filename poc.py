import re

# Initialize empty lists for greetings and goodbyes
greetings = ['hi', 'hello', 'hey', 'greetings', 'good morning', 'good afternoon', 'good evening']
goodbyes = ['bye', 'goodbye', 'see ya', 'see you', 'take care']

# Join the greetings and goodbyes lists into regex patterns
greeting_pattern = re.compile(r"^(" + "|".join(greetings) + ")", re.IGNORECASE)
goodbye_pattern = re.compile(r"^(" + "|".join(goodbyes) + ")", re.IGNORECASE)

while True:
    # Ask for user input
    message = input("Enter a message: ")

    # Use RegEx to detect greetings and add to list if not already present
    match = re.search(greeting_pattern, message)
    if match:
        greeting = match.group().lower()
        if greeting not in greetings:
            confidence = round(len(greeting) / len(message), 2)
            if confidence < 0.8:
                user_input = input(f"Detected a new greeting: {greeting}. Is it a greeting, goodbye, both or neither? ").lower()
                if user_input == 'greeting':
                    greetings.append(greeting)
                    greeting_pattern = re.compile(r"^(" + "|".join(greetings) + ")", re.IGNORECASE)
                elif user_input == 'both':
                    greetings.append(greeting)
                    goodbyes.append(greeting)
                    greeting_pattern = re.compile(r"^(" + "|".join(greetings) + ")", re.IGNORECASE)
                    goodbye_pattern = re.compile(r"^(" + "|".join(goodbyes) + ")", re.IGNORECASE)
                elif user_input == 'neither':
                    pass
                else:
                    print("Invalid input. Message not added.")
                    continue
                print(f"Detected a greeting: {greeting} with confidence level {confidence}")
            else:
                greetings.append(greeting)
                greeting_pattern = re.compile(r"^(" + "|".join(greetings) + ")", re.IGNORECASE)
                print(f"Detected a greeting: {greeting} with confidence level {confidence}")

    # Use RegEx to detect goodbyes and add to list if not already present
    match = re.search(goodbye_pattern, message)
    if match:
        goodbye = match.group().lower()
        if goodbye not in goodbyes:
            confidence = round(len(goodbye) / len(message), 2)
            if confidence < 0.8:
                user_input = input(f"Detected a new goodbye: {goodbye}. Is it a greeting, goodbye, both or neither? ").lower()
                if user_input == 'goodbye':
                    goodbyes.append(goodbye)
                    goodbye_pattern = re.compile(r"^(" + "|".join(goodbyes) + ")", re.IGNORECASE)
                elif user_input == 'both':
                    goodbyes.append(goodbye)
                    greetings.append(goodbye)
                    goodbye_pattern = re.compile(r"^(" + "|".join(goodbyes) + ")", re.IGNORECASE)
                    greeting_pattern = re.compile(r"^(" + "|".join(greetings) + ")", re.IGNORECASE)
                elif user_input == 'neither':
                    pass
                else:
                    print("Invalid input. Message not added.")
                    continue
                print(f"Detected a goodbye: {goodbye} with confidence level {confidence}")
            else:
                goodbyes.append(goodbye)
                goodbye_pattern = re.compile(r"^(" + "|".join(goodbyes) + ")", re.IGNORECASE)
        print(f"Detected a goodbye: {goodbye} with confidence level {confidence}")