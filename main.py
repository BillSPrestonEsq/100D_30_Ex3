import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)

word = input("Enter a word: ").upper()
invalid_input = True
while invalid_input:
    try:
        output_list = [phonetic_dict[letter] for letter in word]
        invalid_input = False
    except KeyError:
        print("Only letters in the alphabet please")
        word = input("Enter a word: ").upper()
    else:
        print(output_list)
