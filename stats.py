def count_words(book):
    words = book.split()
    return len(words)

def count_charaters(book):
    characters = {}
    for char in book:
        char = char.lower()
        if char not in characters:
            characters[char] = 1
        else:
            characters[char] += 1
    return characters

def sort_characters(characters):
    list_of_dictionaries = []
    for c in characters:
        new_dict = {"char": c, "num": characters[c]}
        list_of_dictionaries.append(new_dict)
    def sort_on(items):
        return items["num"]
        
    list_of_dictionaries.sort(reverse=True, key=sort_on)
    return list_of_dictionaries
