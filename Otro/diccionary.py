import json

# load the dictionaries from a JSON file
with open("words.json") as file:
    data = json.load(file)
    verbs = data["verbs"]
    adjectives = data["adjectives"]
    nouns = data["nouns"]
    prepositions = data["prepositions"]

# ask the user if they want to add a new word
new = input("Do you want to register a new word? (y/n) ")
if new.lower() == "y":
    # ask for the type of word and the new word and meaning
    sort = input("What sort of word do you want to register? (verb/adjective/noun/preposition) ")
    new_word = input("Enter the new word: ")
    meaning = input("Enter the meaning: ")

    # add the new word to the appropriate dictionary
    if sort.lower() == "verb":
        verbs[new_word] = meaning
    elif sort.lower() == "adjective":
        adjectives[new_word] = meaning
    elif sort.lower() == "noun":
        nouns[new_word] = meaning
    elif sort.lower() == "preposition":
        prepositions[new_word] = meaning
    else:
        print("Invalid input.")

    # save the dictionaries to the JSON file
    with open("words.json", "w") as file:
        data = {"verbs": verbs, "adjetives": adjectives, "nouns": nouns, "prepositions": prepositions}
        json.dump(data, file)

# ask the user if they want to see the list of words
tosee = input("Do you want to check something? (y/n) ")

if tosee.lower() == "y":
    # ask for the type of words want to be seen
    ok = input("What list do you want to see? (verbs/adjectives/nouns/prepositions) ")

    # print the list of words and meanings
    if ok.lower()=="verbs":
        for verb, meaning in verbs.items():
            print(verb,"->", meaning)
    elif ok.lower()=="nouns":
        for noun, meaning in nouns.items():
            print(noun,"->", meaning)
    elif ok.lower()=="adjectives":
        for adj, meaning in adjectives.items():
            print(adj,"->", meaning)
    elif ok.lower()=="prepositions":
        for prep, meaning in prepositions.items():
            print(prep,"->", meaning)
