# c:\Users\admin\Desktop\Ri\news name detection.py
# news name detection.py
# main.py
import spacy

# Load the small English model
nlp = spacy.load("en_core_web_sm")

# Sample news headlines or user input
texts = [
    "Apple is planning to buy a London-based AI startup for $1 billion.",
    "Narendra Modi met Elon Musk in San Francisco.",
    "Google launches new AI lab in Bengaluru, India."
]

# Process each sentence and extract named entities
for text in texts:
    doc = nlp(text)
    print(f"\nText: {text}")
    for ent in doc.ents:
        print(f" - {ent.text} ({ent.label_})")
