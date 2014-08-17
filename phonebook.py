# A mini phonebook Python app based off the coding exercise written
    # by Amy Hanlon (HS W '14)

import os
import cPickle

class ArgumentError(Exception): pass

class NoFileError(Exception): pass

class DuplicateError(Exception): pass

def create(phonebook_name):
    """Creates a new phonebook of the given name (as .txt file)."""
    filename = phonebook_name + ".txt"

    if os.path.exists(filename):
        raise DuplicateError("That phonebook already exists!")
    else:
        with open(filename, "w") as infile:
            pass

def add(name, number, phonebook):
    """Adds new entry to specified phonebook."""
    phonebook_data = phonebook_exists(phonebook)

    phonebook_data[name] = number
    print phonebook_data
    save(phonebook_data, phonebook)


def update(name, number, phonebook):
    """Updates an entry of given name with new number."""
    pass

def lookup(name, phonebook):
    """Given name, returns any matching entries."""

    phonebook_data = phonebook_exists(phonebook)

    match = False
    for key in phonebook_data:
        if key.lower().find(name.lower()) > -1:
            match = True
            print key, phonebook_data[key]

    if not match:
        print "No matches found."

def reverse_lookup(number, phonebook):
    """Given number, returns matching entry (exact match only)."""

    phonebook_data = phonebook_exists(phonebook)

    match = False
    for key, value in phonebook_data.iteritems():
        if value.find(number) > -1:
            print key, value
            match = True
            break

    if not match:
        print "No matches found."

# TODO: lookup_exact and reverse_lookup_exact?

def check_num_format(number):
    """Checks if a phone number is the right length/format."""
    pass

def phonebook_exists(phonebook):
    """Returns the dictionary of names/numbers contained in the given
        phonebook file, or throws an error if the file does not exist."""
    filename = phonebook + ".txt"
    if not os.path.exists(filename):
        raise NoFileError("That phonebook doesn not exist!")
    else:
        with open(filename) as infile:
            return cPickle.load(infile)

def save(data, phonebook):
    """Saves the dictionary containing phonebook data to the given
        phonebook, using cPickle."""
    filename = phonebook + ".txt"

    with open(filename, "w") as outfile:
        cPickle.dump(data, outfile)

def main():
    """The main function of the program."""
    pass

if __name__ == '__main__':
    main()