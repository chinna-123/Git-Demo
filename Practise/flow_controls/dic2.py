famous_songs = {"Queen": "Bohemian Rhapsody",
                "Bee Gees": "Stayin' Alive",
                "U2": "One",
                "Michael Jackson": "Billie Jean",
                "The Beatles": "Hey Jude",
                "Bob Dylan": "Like A Rolling Stone"}
print(len(famous_songs))
for key in famous_songs.keys():
    print(key)
print(famous_songs.values())
for key, value in famous_songs.items():
    print(key, value)
print(famous_songs.get("Promise of the Real", "That is not a key that appears in the dictionary."))
tuple_t = (1, 3, 5)
list_l = [1, 3, 5]
print(tuple_t.__sizeof__())
print(list_l.__sizeof__())