def calculate_project_cost(hours, hourly_rate):
    project_cost = hours * hourly_rate
    return project_cost

results = calculate_project_cost(12, 500)

print("project_cost:", results)