import json
import re
import fasttext
from huggingface_hub import hf_hub_download

model_path = hf_hub_download(repo_id="facebook/fasttext-language-identification", filename="model.bin")
model = fasttext.load_model(model_path)

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

# Iterate over the terms and detect their language
for item in terms:
    word = item["term"]
    languageString = detect_language(word)
    print(languageString)
    if 'eng' in languageString and is_meaningful_word(word):
        english_loanwords.append(item)

# Save the list of English loanwords to a JSON file
with open('fasttext_result.json', 'w', encoding='utf-8') as file:
    json.dump(english_loanwords, file, ensure_ascii=False, indent=4)

# Print a message indicating the loanwords have been saved
print("English loanwords saved to 'fasttext_result.json'")
