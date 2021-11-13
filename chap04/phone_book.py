def find_phonenumber(phonebook, name):
    for n, p in phonebook:
        if n == name:
            return p
    return None