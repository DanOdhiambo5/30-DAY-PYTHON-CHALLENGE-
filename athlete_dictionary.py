athlete = {
    "name": "John",
    "age": 25,
    "sport": "Football",
    "sleep_hours": 7.5
}

# Print the entire dictionary.
print("Athlete details:", athlete)

# Access individual values using their keys.
print("Name:", athlete["name"])
print("Age:", athlete["age"])
print("Sport:", athlete["sport"])

# Add a new key-value pair.
athlete["water_glasses"] = 8

# Update an existing value.
athlete["age"] = 26

# Print the updated dictionary.
print("Updated athlete:", athlete)