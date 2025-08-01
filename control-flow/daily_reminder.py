task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        priority_message = "high priority"
    case "medium":
        priority_message = "medium priority"
    case "low":
        priority_message = "low priority"

match time_bound:
    case "yes":
        time_message = "requires immediate attention today!"
    case "no":
        time_message = "Consider completing it when you have free time."
print(f"Reminder: '{task}' is a {priority_message} task that {time_message}")
