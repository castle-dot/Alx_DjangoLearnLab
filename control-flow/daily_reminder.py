task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

if priority == "high":
    priority_message = "high priority"
elif priority == "medium":
    priority_message = "medium priority"
elif priority == "low":
    priority_message = "low priority"
else:
    priority_message = "unknown priority"

if time_bound == "yes":
    time_message = "requires immediate attention today!"
else:
    time_message = "Consider completing it when you have free time."

print(f"Reminder: '{task}' is a {priority_message} task that {time_message}")
