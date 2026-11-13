# STEP 1: Create a list containing athlete records.
# Each athlete is stored as a dictionary with a name, age and score

athletes = [
    {"name": "Brian", "age": 24, "score": 85},
    {"name": "Kevin", "age": 22, "score": 90},
    {"name": "Mary", "age": 25, "score": 78}
]

# STEP 2: Create a function to display all athletes.
# The for loop goes through each athlete and prints their details.

def display_athletes():
    for athlete in athletes:
        print(athlete["name"], athlete["age"], athlete["score"])

# STEP 3: Display the original list of athletes.


display_athletes()

# STEP 4: Create a function to calculate the average score.
# Add all athlete scores, then divide by the number of athletes.

def calculate_average_score():
    total = 0

    for athlete in athletes:
        total += athlete["score"]

    average = total / len(athletes)

    return average

# STEP 5: Display the average score returned by the function.

print("Average score:", calculate_average_score())

# STEP 6: Create a function to find the athlete with the highest score.
# Assume the first athlete has the highest score.
# Compare every other athlete's score against the current highest score.

def find_top_athlete():
    top_athlete = athletes[0]

    for athlete in athletes:
        if athlete["score"] > top_athlete["score"]:
            top_athlete = athlete

    return top_athlete

# STEP 7: Call the function and display the top athlete's details.

top = find_top_athlete()

print("Top athlete:", top["name"])
print("Highest score:", top["score"])

# STEP 8: Create a function to add a new athlete.
# Parameters receive the athlete's name, age and score.
# The append() method adds the new dictionary to the athletes lis

def add_athlete(name, age, score):
    new_athlete = {
        "name": name,
        "age": age,
        "score": score
    }

    athletes.append(new_athlete)

# STEP 9: Add James to the athlete database.

add_athlete("James", 23, 95)

# STEP 10: Display the updated athlete list.

print("\nUpdated athlete list:")
display_athletes()
print("New average score:", calculate_average_score())

# STEP 12: Create a function to search for an athlete by name.
# The lower() method makes the search case-insensitive.
# Return the matching athlete if found, otherwise return None.

def search_athlete(name):
    for athlete in athletes:
        if athlete["name"].lower() == name.lower():
            return athlete

    return None

# STEP 13: Search for James and display the result.
# If the search returns an athlete, display their details.
# Otherwise, display a message saying the athlete was not found.

result = search_athlete("James")

if result:
    print("Athlete found:", result["name"])
    print("Score:", result["score"])
else:
    print("Athlete not found")


