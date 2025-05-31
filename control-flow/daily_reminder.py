# Create a simplified Python script that uses conditional statements, Match Case, and loops to remind the user about a single, priority task for the day based on time sensitivity.
# daily_reminder.py

task = input("Enter the task description: ")
priority = input("Enter the task priority (high, medium, low): ").lower()
time_bound = input("Is the task time-bound? (yes or no): ").lower()

print("\n--- Daily Reminder ---")

match priority:
    case "high":
        message = f"Task: {task} [HIGH PRIORITY]"
    case "medium":
        message = f"Task: {task} [Medium Priority]"
    case "low":
        message = f"Task: {task} [Low Priority]"
    case _:
        message = f"Task: {task} [Unknown Priority]"
if time_bound == "yes":
    message += " — This task requires immediate attention today!"

# Display the final reminder
print(message)
