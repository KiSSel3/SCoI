import constants

import collections
import re

def amount_of_sentences(text:str):
    sentences = re.findall(constants.SENTENCES_PATTERN, text)
    abbreviation = re.findall(constants.ABBREVIATION, text)

    return len(sentences) - len(abbreviation) * 2


def amount_of_non_declarative_sentences(text:str):
    sentences = re.findall(constants.NON_DECLARATIVE_PATTERN, text)

    return len(sentences)


def words_list(text:str):
    words = re.findall(constants.WORDS_PATTERN, text)
    return words


def average_amount_of_characters_in_sentence(text:str):
    amount_sentences = amount_of_sentences(text)
    words = words_list(text)
    amount_characters_in_word = 0

    for word in words:
        amount_characters_in_word += len(word)

    if amount_sentences != 0:
        return amount_characters_in_word / amount_sentences
    return 0


def average_amount_of_characters_in_word(text:str):
    words = words_list(text)
    amount_characters_in_word = 0

    for word in words:
        amount_characters_in_word += len(word)

    if len(words) != 0:
        return amount_characters_in_word / len(words)
    return 0


def top_grams(text:str, k:int = 10, n:int = 4):
    n_grams: dict[str, int] = {}
    words = [word.lower() for word in words_list(text)]
    for word_index in range(len(words) - int(n) + 1):
        n_gram = ' '.join(str(word) for word in words[word_index:word_index + int(n)])
        if n_gram in n_grams:
            n_grams[n_gram] += 1
        else:
            n_grams[n_gram] = 1
    sorted_n_grams = sorted(n_grams.items(), reverse=True, key=lambda item: item[1])
    result = sorted_n_grams[:int(k)]
    return result