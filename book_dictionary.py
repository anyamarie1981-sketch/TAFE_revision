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

# - DEFINED FUNCTIONS -

def find_value(inner_dict, inner_key):
    for key, value in inner_dict.items():
        if key == inner_key:
            return value
        elif isinstance(value, dict):
            result = find_value(value, inner_key)
            if result:
                return result
    return None

def title_case(s):
    return s.strip().casefold()

def check_title(data, title_for_check):
    book = title_case(title_for_check)
    if isinstance(data, dict):
        if "Title" in data and title_case(str(data["Title"])) == book:
            return data
        for value in data.values():
            found = check_title(value, title_for_check)
            if found is not None:
                return found
    elif isinstance(data, list):
        for item in data:
            found = check_title(item, title_for_check)
            if found is not None:
                return found

    return None

def print_loop():
    for record_num, details in media_dict.items():
        line_1 = []
        for key, value in details.items():
            line_1.append(f"{key}: {value}")
        print(f"Book {record_num}: " + ", ".join(line_1))

def allocate_parts_to_keys(parts, keys):
    book = {}
    for part in parts:
        print(f"\nValue: {part}")
        print("""
Which key should this be assigned to?
1 = Title
2 = Author(s)
3 = Genre
4 = Opinion
0 - Skip              
""")
        while True:
            choice = input("Enter number: ").strip()
            if choice == "0":
                break
            if not choice.isdigit():
                print("Please enter a number from 0-4")
                continue
            index = int(choice) - 1
            if index < 0 or index >= 4:
                print("Please enter a number from 0-4")
                continue
            selected_key = keys[index]
            if selected_key in book:
                print(f"'{selected_key}' already has a value. Choose another key")
            else:
                book[selected_key] = part
                break
        

    return book

            



# - INPUT LOOP -
while True:
    raw_input = input(
        "\nEnter the Book Title, Author(s) Genre & your review. "
        "Each section should be seperated by a comma ',' " 
        "Do not use commas in your information sections: "
    )
    if raw_input == "":
        break

    parts = [p.strip() for p in raw_input.split(",")]

    if len(parts) != 4:
        print("\nInput error: data is not in groups of 4. Unable to automatically allocate to keys.")
        print(parts)
        new_entry = allocate_parts_to_keys(parts, keys)

    else:
         new_entry = {
        "Title": parts[0],
        "Author(s)": parts[1],
        "Genre": parts[2],
        "Opinion": parts[3],
    }           

    existing_book = check_title(media_dict, new_entry["Title"])

    if existing_book is not None:
            print(f"'{new_entry["Title"]}' already exists")
            choice = input("Do you want to update the existing entry? (y/n): ").strip().lower()

            if choice in ("y", "yes"):
                existing_book.update(new_entry)
                print("Entry updated")
                print_loop()
            else:
                print("Update cancelled")
            continue
    next_id = max(media_dict.keys(), default=0) + 1
    media_dict[next_id] = new_entry
    print("\nNew entry added")
    print_loop()


# - PRINTING -
print("\nBook Reading List")
print_loop()

# for title in media:
#     # Do something fun here, if you like, but try outputting your data again.
#     pass
