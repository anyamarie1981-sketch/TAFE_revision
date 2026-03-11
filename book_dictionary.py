

"""
In this file, let's build a list of all the books we've read (or movies we've 
watched or games we've played -- doesn't matter) in the last few months.

Assuming that you receive a comma-separated list of the name, genre, a note about your 
reaction to it, try storing it in a *structured* way.

That is to say, if I input:
Tears of the Kingdom,Action-adventure,Loved a lot but a bit over-rated in places
Cult of the Lamb,Roguelike,Probably played too much of this one
Cities:Skylines,Simulation,Classic

Then I want to see a list like this:
media = [
    { name: "Tears of the Kingdom", genre: "Action-adventure", opinion: "Loved a lot but a bit over-rated in places" },
    { name: "Cult of the Lamb", genre: "Roguelike", opinion: "Probably played too much of this one" },
    { name: "Cities:Skylines", genre: "Simulation", opinion: "Classic" },
]

We *could* have made this a list-of-lists, but by making a list of dictionaries, we can trust that the data is structured 
when we go to use it.
"""
# starting variables
keys = ["Title", "Author(s)", "Genre", "Opinion"]
media = []
media_dict = {}

# -------- INPUT LOOP --------
while True:
    raw_input = input(
        "Enter the Book Title, Author(s) Genre & your review. "
        "Each section should be seperated by a comma ',': "
    )
    if raw_input == "":
        break
    

    for value in raw_input.split(","):
        new_value = value.strip()
        if new_value in media:
            print("Book already entered. Please enter a different book.")
        else:               
            media.append(new_value)
        print(new_value)
        

# -------- PROCESSING --------
if len(media) % 4 != 0:
    print("Input error: data is not in groups of 4")
else:
    index = 0
    while index < len(media):
        current_record = {
            keys[0]: media[index],
            keys[1]: media[index + 1],
            keys[2]: media[index + 2],
            keys[3]: media[index + 3],
        }
        [index // 4 + 1] = current_record
        index += 4

# -------- PRINTING --------
        for record_num, details in media_dict.items():
            line = []
            for key, value in details.items():
                line.append(f"{key}: {value}")
            print(f"Book {record_num}: " + ", ".join(line))

    

    




# for title in media:
#     # Do something fun here, if you like, but try outputting your data again.
#     pass
