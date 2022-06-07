import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter : row.code for (index, row) in data.iterrows()}

print(phonetic_dict)


def generate_phonetic():
    word = input("Please enter a word: ").upper()

    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("letters in the alphabet only!")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()

