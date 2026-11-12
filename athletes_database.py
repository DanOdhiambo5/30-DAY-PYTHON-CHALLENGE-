athletes = [
    {
        "name": "John",
        "age": 25,
        "sport": "Football"
    },
    {
        "name": "Peter",
        "age": 23,
        "sport": "Basketball"
    },
    {
        "name": "David",
        "age": 27,
        "sport": "Athletics"
    }
]

# Print all athletes.
for athlete in athletes:
    print("Name:", athlete["name"])
    print("Age:", athlete["age"])
    print("Sport:", athlete["sport"])
    print("--------------------")

# Add another athlete.
athletes.append({
    "name": "Brian",
    "age": 24,
    "sport": "Swimming"
})

print("Total athletes:", len(athletes))
