from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    return open(file_path).read()


def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    text_string = text_string.split()

    chains = {}

    for word_index in range(len(text_string) - 1):
        try:
            first_word = text_string[word_index]
            second_word = text_string[word_index + 1]
            value = text_string[word_index + 2]

            if (first_word, second_word) in chains:
                chains[(first_word, second_word)].append(value)
            else:
                chains[(first_word, second_word)] = [value]

        except IndexError:
            pass

    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    starting_point = choice(chains.keys())

    text = " ".join(starting_point)

    new_key = (starting_point[1], choice(chains[starting_point]))
    text += " " + new_key[1]
    
    while new_key in chains:
            new_key = (new_key[1], choice(chains[new_key]))
            text += " " + new_key[1]
        
    return text


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
