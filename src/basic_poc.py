import nltk
import random
from nltk.tokenize import regexp_tokenize
import re

# Define the patterns and responses for the chatbot
patterns = {
    r"\bhi\b|\bhello\b|\bhey\b|\bwhassup\b|\bsup\b|\bwassup\b|\bwhat('s| is)\b \bup\b|\bahoy\b|\bwhats\b \bup\b": ['Hello!', 'Hi there!', 'Hey!'],
    r"\bwhat('s| is)\b \byour\b \bname\??\b": ['My name is LuminaNMP-1.', 'I am LuminaNMP-1.'],
    r"\bhow\b \bare\b \byou\??\b|\bhow\b \bare\b \byou\b \bdoin('|g)\??\b|\bhow\b \bdo\b \byou\b \bfeel\??\b": ['I am doing well, thank you!', 'I am good, thanks for asking.'],
    r"\bbye\b|\bgoodbye\b|\bgood\b \bbye\b|\bsee\b \b(u|you|ya)\b|\bcy(a|ou)\b|\blater\b|\blaters\b": ['Goodbye!', 'See you later!', 'Bye!', 'See you later!'],
}

# Define regular expressions to match specific patterns
patterns_re = {}
for pattern, responses in patterns.items():
    pattern_re = '|'.join([f'({w})' for w in pattern.split('|')])
    patterns_re[pattern_re] = responses

# Add conjunctions to the regular expression pattern
conjunctions = r'\b(and|or|but)\b'
pattern_re = '|'.join([f'({w})' for w in patterns.keys()]) + f'|{conjunctions}'
patterns_re[pattern_re] = random.choice(list(patterns.values()))

# Start the chatbot conversation
print("Hi, I'm LuminaNMP-1. How can I help you today?")
while True:
    user_input = input('> ')
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
        response = random.choice(patterns_re[matched_pattern])
    else:
        response = "I'm sorry, I don't understand."
    
    print(response)