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
# - Defined Functions -
def example_book():
    print("To Kill A Mocking Bird, Harper Lee, Southern Gothic / Coming of Age, 4/5, " \
    "A timeless American masterpiece offering a powerful coming-in-age look at racial " \
    "injustice and lost innocence in the 1930s South through young Scout’s eyes")

def normalise_text(s):
    return s.strip().upper()

def print_loop():
   for record_num, details in media_dict.items():
        line_1 = []
        for key, value in details.items():
            line_1.append(f"{key}: {value}")
        print(f"BOOK {record_num}: " + ", ".join(line_1)) 

def allocate_parts(parts, keys):
    book = {}
    for part in parts:
        print(f"Value: {part}")
        print("""
Which Key should this be assigned to ?
1 = Title
2 = Author(s)
3 = Genre
4 = Rating
5 = Opinion
0 - Skip""")
        while True:
            key_choice = input("Enter number: ").strip()
            if key_choice == "0":
                break
            if not key_choice.isdigit():
                print("Please enter a number from 0 to 5")
                continue
            elif int(key_choice) > 5:
                print("Please enter a number from 0 to 5")
                continue
            index = int(key_choice) - 1
            selected_key = keys[index]
            if selected_key in book:
                print(f"{selected_key} already has a value. Select another key")
            else:
                book[selected_key] = part
                break
#   print("Allocation Complete")    #debug line
#   print(book)                     #debug line
    return book

def next_id():
    next_id = max(media_dict.keys(), default=0) + 1
    return next_id

    
 
# - dictionaries & lists -

media = []
media_dict = {}
keys = ("Title", "Author(s)", "Genre", "Rating /5", "Review")


# - program -

while True:
    raw_input = input("""
Enter the Book Title, Author(s), Genre, Rating /5 & your review. 
Enter D for an example, Q to exit
Each section should be separated by a comma ','
Comma's should not be used elsewhere in the text: """)
    
    normal_input = normalise_text(raw_input)
#    print(normal_input)    #debug line
    parts = normal_input.split(",")
#    print(parts)           #debug line
    
    if normal_input == "Q":
        break

    elif normal_input == "D":
        example_book()
        continue
  
    elif len(parts) % 5 != 0:
        print("Sections are missing, please review entry")
        media_dict[next_id()] = allocate_parts(parts, keys)
        print_loop()
        continue

#   elif  #placeholder for check if title exists 

    new_entry = {
        "Title": parts[0],
        "Author(s)": parts[1],
        "Genre": parts[2],
        "Rating /5": parts[3],
        "Review": parts[4]
    }

    media_dict[next_id()] = new_entry
    print("\nNew entry added")
    print_loop()

    

   


# for title in media:
#     # Do something fun here, if you like, but try outputting your data again.
#     pass