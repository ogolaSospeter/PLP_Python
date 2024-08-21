import json
from difflib import get_close_matches

# Load the dictionary data from the JSON file
def load_dictionary(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Fetch the definition for a word from the dictionary
def get_definition(word, dictionary_data):
    word = word.lower()
    if word in dictionary_data:
        definitions = dictionary_data[word]
        formatted_definitions = "\n".join([f"{i+1}. {definition}" for i, definition in enumerate(definitions)])
        return formatted_definitions
    else:
        # Find close matches for the misspelled word
        suggestions = get_close_matches(word, dictionary_data.keys(), n=3, cutoff=0.8)
        if suggestions:
            return f"Word not found. Did you mean: {', '.join(suggestions)}?"
        else:
            return "Word not found and no suggestions available."

def main():
    dictionary_data = load_dictionary('data.json')
    print("Welcome to the Dictionary!")
    while True:
        word = input("Enter a word to find its definition (or type 'exit' to quit): ").strip()
        if word.lower() == 'exit':
            print("Goodbye!")
            break
        definition = get_definition(word, dictionary_data)
        print(definition)

if __name__ == "__main__":
    main()
