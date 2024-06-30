task = input("Enter your task:")
priority = input("priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: {task} is high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: {task} is high priority task but you can find time later today")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: {task} is medium priority, complete by tomorrow")
        else:
            print(f"Reminder: {task} is medium priority, find time the day after tomorrow")
    case "low":
        if time_bound== "yes":
            print(f"Reminder: {task} is low priority, find time at the end of the week to complete task" )
        else:
            print(f"Reminder: {task} is low priority find time next month")
