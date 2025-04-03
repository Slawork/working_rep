import re

def abbreviate_sentence(sentence):
    pattern = re.compile(r'\b([a-z]{3})'r'([^aeiou]*)' r'([aeiou][a-z]*)\b',re.IGNORECASE    )

    return pattern.sub(r'\1\2.', sentence)

input_text = "Hello! I love dogs ."
output_text = abbreviate_sentence(input_text)
print(output_text)