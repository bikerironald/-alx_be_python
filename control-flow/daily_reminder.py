# Create a simplified Python script that uses conditional statements, Match Case, and loops to remind the user about a single, priority task for the day based on time sensitivity.
# daily_reminder.py

Task = input("Enter the task description: ")
Priority = input("Enter the task priority (high/medium/low): ").strip().lower()
Time_bound = input("Is the task time-bound? (yes/no): ").strip().lower()

print("\n--- Daily Reminder ---")

match Priority:
    case "high":
        message = f"Task: {Task} [HIGH PRIORITTask]"
        message = f"Task: {Task} [Medium Priority]"
    case "low":
        message = f"Task: {Task} [Low Priority]"
    case _:
        message = f"Task: {Task} [Unknown Priority]"
if Time_bound == "yes":
    message += " — This task requires immediate attention today!"

# Display the final reminder
print(message)
