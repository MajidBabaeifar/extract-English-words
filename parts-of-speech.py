import nltk
from collections import Counter
import json



# Download necessary resources
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('punkt_tab')

# Function to read a text file and perform tokenization and POS tagging
def process_text_file(file_path):
    # Open and read the content of the file
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # Tokenize the text and perform POS tagging
    words = nltk.word_tokenize(text, language='german')
    pos_tags = nltk.pos_tag(words)
    
    return pos_tags

# Replace with the path to your text file
file_path = 'project sources/all txt/boulivard/Dienstag.txt'

# Process the file and print POS tags
pos_tags = process_text_file(file_path)

# Count occurrences of each tuple
counter = Counter(pos_tags)

# Convert back to a list with counts
result = [(item, count) for item, count in counter.items()]

# Display the result
print(result)



# Step 1: Load second list from a JSON file
with open('fasttext_result.json', 'r') as file:
    english_words = json.load(file)

# Your first list of tuples


# Step 2: Apply the matching algorithm
for item in english_words:
    item['pos'] = []
    for tuple_element in result:
        if item['term'] == tuple_element[0][0]:  # Match term with the first element of the tuple
            item['pos'].append({'role': tuple_element[0][1], 'repeat':tuple_element[1] })

# Step 3: (Optional) Save updated second list back to a file
with open('fasttext-pos-result.json', 'w') as file:
    json.dump(english_words, file, indent=4)
