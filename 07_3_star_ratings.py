"""
You have a collection of titles.

You are manually inputing ratings (1-5) for each title -- but there's a catch:
You are putting in ratings by many different people. At the end, I want
to be able to see the minimum rating, the maximum rating, and the average
rating of any particular title.

Inputs will have a title, a comma, and then the rating for that particular input.

You will need to use a mix of string functions, dictionary functions, and list functions.

A set of example inputs, line-by-line, might be like this:
```
Humans and Rats,1
Humans and Rats,5
Serpents and Strangers,3
Hunted by the Swamp,5
Hunted by the Swamp,2
Hunted by the Swamp,4
Humans and Rats,5
```

I would expect your output to read something like this (title order does not matter):
```
'Humans and Rats' had a minimum score of 1, a maximum score of 5, and averaged 3.6666666666666665.
'Serpents and Strangers' had a minimum score of 3, a maximum score of 3, and averaged 3.
'Hunted by the Swamp' had a minimum score of 2, a maximum score of 5, and averaged 3.6666666666666665.
```

Extension!
(You'll need to do a little research about rounding)
Those averages look a bit ugly, please instead output them to 2 decimal places, eg:
'Hunted by the Swamp' had a minimum score of 2, a maximum score of 5, and averaged 3.67.

Extension 2:
See how you might factor this into functions to improve readability.
"""
# - Starting Variables -
ratings = []
dictionary_keys = ("Title", "Rating")

# - Defined Functions - 

def normal_text(s):
    return s.strip().casefold()


def check_title(ratings, entry_check):
    entry = normal_text(entry_check)
    for item in ratings:
        if normal_text(item["Title"]) == entry:
            return item
    return None

def print_loop():
    for entry in ratings:
        title = entry["Title"].upper()
        ratings_list = entry["Rating"]
        calcs = rating_calc(entry)
        print(f"\"{title}\" had ratings {ratings_list}.")
        print(f"The minimum rating was: {calcs["min"]};" 
              f" The maximum rating was: {calcs["max"]};"
              f" The average rating was: {calcs["avg"]}")
        # print(type(ratings))
        # print(ratings)

# def rating_min():
#     for entry in ratings:
#         minimum = min(entry["Rating"])
#     return minimum        

# def rating_max():
#     for entry in ratings:
#         maximum = max(entry["Rating"])
#     return maximum  

# def rating_avg():
#     for entry in ratings:
#         average = sum(entry["Rating"]) / len(entry["Rating"])
#         round_average = round(float(average), 2)
#     return round_average  

def rating_calc(entry):
    ratings = entry["Rating"]
    return {
        "min": min(ratings),
        "max": max(ratings),
        "avg": round(sum(ratings) / len(ratings), 2)
    }


# - Input Loop -
print("""
Enter a Title followed by a rating. Ratings are out of 5.
This should be in the format: Title, Number
Example: Frankenstein, 5   
""")
while True:
    raw_input = input("Title and rating: ")
    if raw_input == "":
        break
    normal_input = normal_text(raw_input)
#    print(normal_input)      #debug line
    parts = normal_input.split(",")
#    print(parts)            #debug line
 
    if len(parts) % 2 != 0:
        print("Please re-enter your title and rating")
        continue
    try:
        num_check = int(parts[1])
        print(f"num_check: {num_check}")
    except ValueError:
        print("Rating must be a number from 0-5")
        continue 
    if not (0 <= num_check <= 5):
        print("Rating must be a number from 0-5")
        continue 

    else:
        new_title = {
            "Title": parts[0],
            "Rating": [num_check]
        }
    #        print(f"new-title: {new_title}")        #debug line

    #    print("ratings type:", type(ratings), ratings)

    existing_entry = check_title(ratings, parts[0])

    if existing_entry is not None:
        existing_entry["Rating"].append(num_check)
        print("\nEntry updated")
        print_loop()
        continue
    else:
        ratings.append(new_title)
        print("\nEntry added")
        print_loop()
print(f"Dictionary: {ratings}")



    # Here, get your title and rating

    # Do some data checking -- you want to make sure your rating is a number, after all:



    # Once you're done, you'll need to go through your list of ratings and output the format:
    # for title, rating_list in ratings.items():
    # pass # Replace this line


