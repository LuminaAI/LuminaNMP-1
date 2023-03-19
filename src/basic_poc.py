import nltk
import random
from nltk.tokenize import regexp_tokenize
import re
import getpass

# Define the patterns and responses for the chatbot
patterns = {
    r"\bhi\b|\bhello\b|\bhey\b|\bwhassup\b|\bsup\b|\bwassup\b|\bwhat('s| is)\b \bup\b|\bahoy\b|\bwhats\b \bup\b|\bgreetings\b": ['Hello!', 'Hi there!', 'Hey!', 'Greetings!', 'Good day!', 'Nice to see you!', 'Hey there!'],
    r"\bwhat('s| is)\b \byour\b \bname\??\b": ['My name is LuminaNMP-1.', 'I am LuminaNMP-1.', 'You can call me Lumina.', 'I go by LuminaNMP-1.', 'LuminaNMP-1 is my name.'],
    r"\bhow\b \bare\b \byou\??\b|\bhow\b \bare\b \byou\b \bdoin('|g)\??\b|\bhow\b \bdo\b \byou\b \bfeel\??\b": ['I am doing well, thank you!', 'I am good, thanks for asking.', 'I feel great!', 'I am functioning properly.', 'I am well, how about you?', 'I am feeling wonderful, thank you for asking.'],
    r"\bbye\b|\bgoodbye\b|\bgood\b \bbye\b|\bsee\b \b(u|you|ya)\b|\bcy(a|ou)\b|\blater\b|\blaters\b|\bsee you soon\b|\badios\b": ['Goodbye!', 'See you later!', 'Bye!', 'See you later!', 'Farewell!', 'Take care!', 'Until next time!', 'Bye-bye!', 'Have a good day!', 'Catch you later.'],
}

# Define regular expressions to match specific patterns
patterns_re = {}
for pattern, responses in patterns.items():
    pattern_re = '|'.join([f'({w})' for w in pattern.split('|')])
    patterns_re[pattern_re] = responses

# Add conjunctions and pronouns to the regular expression pattern
conjunctions = r'\b(and|or|but)\b'
pronouns = r'\b(i|you|he|she|it|we|they)\b'
pattern_re = '|'.join([f'({w})' for w in patterns.keys()]) + f'|{conjunctions}|{pronouns}'
patterns_re[pattern_re] = random.choice(list(patterns.values()))

# Start the chatbot conversation
print("Hi, I'm LuminaNMP-1. How can I help you today?")
while True:
    user_input = input(f'{getpass.getuser()} > ')
    if user_input.lower() in ['exit', 'quit']:
        break
    
    # Tokenize user input
    tokens = regexp_tokenize(user_input.lower(), r'\w+|[\&\|\^]+')
    
    # Match patterns in user input
    matched_pattern = None
    for pattern_re, responses in patterns_re.items():
        if re.search(pattern_re, user_input.lower()):
            matched_pattern = pattern_re
            break
    
    # Generate a response based on the matched pattern
    if matched_pattern is not None:
        responses = patterns_re[matched_pattern]
        response = random.choice(responses)
    
    else:

        response = "I'm sorry, I don't understand."

    print(f'LuminaNMP-1 > {response}\n')