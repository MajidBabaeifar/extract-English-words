import json
import re
import fasttext

# Load the FastText model
model = fasttext.load_model('lid218e.bin')

# Define a function to detect the language of a word
def detect_language(word):
    lang = model.predict(word)[0][0]
    return lang

# Exclude short terms, terms that are just digits, unwanted patterns (like numbers, years, quantities), and German words
def is_meaningful_word(word):
    # Regex pattern to match numbers, quantities, years, or other non-meaningful terms
    pattern = r'(\d+[,.]?\d*|[A-Za-z]+\d+|\d{4}[a-zA-Z]+|[A-Za-z]+\d+|[\d]+kg|[\d]+ic|[\d]+artikel|\d{2,4}[,.]?\d*)'
    
    # If the word matches any of these patterns or is detected as German, it is not meaningful
    return len(word) > 1 and not re.match(pattern, word)

# Load JSON data from a file
with open('all-words.json', 'r', encoding='utf-8') as file:
    parsed_data = json.load(file)

# Access the terms from the JSON data
terms = parsed_data["corpusTerms"]["terms"]

# Initialize an empty list to store English loanwords
english_loanwords = []
total_instance_count = 0

# Iterate over the terms and detect their language
for item in terms:
    word = item["term"]
    languageString = detect_language(word)
    if 'eng' in languageString and is_meaningful_word(word):
        total_instance_count += item["rawFreq"]
        english_loanwords.append(item)

# Save the list of English loanwords to a JSON file
with open('fasttext_result.json', 'w', encoding='utf-8') as file:
    json.dump(english_loanwords, file, ensure_ascii=False, indent=4)

# Print a message indicating the loanwords have been saved
print(total_instance_count, "total instances and unique number of" , len(english_loanwords), "English loanwords saved to 'fasttext_result.json'")
