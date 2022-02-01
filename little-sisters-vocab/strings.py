"""Little Sister's Vocabulary

https://exercism.org/tracks/python/exercises/little-sisters-vocab

"""
import re


def add_prefix(word: str, prefix: str) -> str:
    """create a word with a prefix.

    :param str word:
    :param str prefix:
    :return: str of root word with un prefix
    """
    return f'{prefix}{word}'


def add_prefix_un(word: str) -> str:
    """

    :param word: str of a root word
    :return:  str of root word with un prefix

    This function takes `word` as a parameter and
    returns a new word with an 'un' prefix.
    """
    return add_prefix(word, 'un')


def make_word_groups(vocab_words: list) -> str:
    """

    :param vocab_words: list of vocabulary words with a prefix.
    :return: str of prefix followed by vocabulary words with
             prefix applied, separated by ' :: '.

    This function takes a `vocab_words` list and returns a string
    with the prefix  and the words with prefix applied, separated
     by ' :: '.
    """
    word_length = len(vocab_words)
    for i in range(1, word_length):
        vocab_words[i] = add_prefix(vocab_words[i], vocab_words[0])

    return ' :: '.join(vocab_words)


def remove_suffix_ness(word: str) -> str:
    """

    :param word: str of word to remove suffix from.
    :return: str of word with suffix removed & spelling adjusted.

    This function takes in a word and returns the base word with `ness` removed.
    """
    return re.sub('i$', 'y', re.sub('ness$', '', word))


def adjective_to_verb(sentence: str, index: int) -> str:
    """

    :param sentence: str that uses the word in sentence
    :param index:  index of the word to remove and transform
    :return:  str word that changes the extracted adjective to a verb.

    A function takes a `sentence` using the
    vocabulary word, and the `index` of the word once that sentence
    is split apart.  The function should return the extracted
    adjective as a verb.
    """
    words = sentence.split()
    target_word = re.sub(r'\.$', '', words[index])
    return f'{target_word}en'
