from spellchecker import SpellChecker

def check_spelling(text):
    # Initialize the spell checker
    spell = SpellChecker()

    # Split the text into words
    words = text.split()

    # Find misspelled words
    misspelled = spell.unknown(words)

    # Display misspelled words and suggestions
    for word in misspelled:
        # Get the most likely correction
        correction = spell.correction(word)
        # Get all possible corrections
        suggestions = spell.candidates(word)
        
        print(f"Misspelled word: {word}")
        print(f"Suggested correction: {correction}")
        print(f"Other suggestions: {suggestions}")
        print()

if __name__ == "__main__":
    # Example paragraph with some intentional spelling mistakes
    paragraph = """Ths is an exmple paragaph with sme speling mistakes.
                   The qick brown fx jmps ovr the lzy dog."""
    
    # Run the spell checker
    check_spelling(paragraph)
