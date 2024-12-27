import nltk

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
print(pos_tags)
