__Author__ = 'AMAR SINGH '

''' sentence break and word sort programme
'''


def break_words(sentence):
    words = sentence.split(' ')
    return words


def sort_words(words):
    return sorted(words)


def first_words(words):
    word = words.pop(0)
    print(f'first_word ::{word}')


def last_words(words):
    word = words.pop(-1)
    print(f'Last Word::{word}')


def sort_sentence(sentance):
    words = break_words(sentance)
    return sort_words(words)


def first_and_last_sentence(sentence):
    words = break_words(sentence)
    first_words(words)
    last_words(words)


def first_and_last_sorted(sentence):
    words = sort_sentence(sentence)
    first_words(words)
    last_words(words)




