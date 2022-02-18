# Imports
import pandas as pd

# Read the Phonetic CSV
data = pd.read_csv("nato_phonetic_alphabet.csv")

phonetic_code_data = {row.letter:row.code for (index, row) in data.iterrows()}

word = input("Enter a word: ").upper()

phonetic_code_words = [phonetic_code_data[w] for w in word]

print(phonetic_code_words)


