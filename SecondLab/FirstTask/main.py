import utilities

if(__name__ == "__main__"):
    file = open('/home/kissel/Programming/SCoI/SecondLab/FirstTask/Text.txt')
    text = file.read()

    print(f'Amount of sentences: {utilities.amount_of_sentences(text)}')
    print(f"Amount of non-declarative sentences: {utilities.amount_of_non_declarative_sentences(text)}")
    print(f"Average amount of characters in sentences: {utilities.average_amount_of_characters_in_sentence(text)}")
    print(f"Average amount of characters in word: {utilities.average_amount_of_characters_in_word(text)}")
    print("Top-K N-grams:")

    k = input("Entered K:")
    while not k.isdigit():
        k = input("Error! Entered K:")

    n = input("Entered N:")
    while not k.isdigit():
        n = input("Error! Entered N:")

    print(utilities.top_grams(text, k, n))
