print("Welcome to the salary calculator by hour")
work_hours = float(input("How many hours per day you work? "))
work_days = int(input("How many days per week do you work? "))
work_hours_per_week = round(work_hours * work_days)
weeks_per_month = int("5")
hours_per_month = work_hours_per_week * weeks_per_month
print(f"You work {hours_per_month} hours per month")
monthly_salary = int(input(f"Now considering you work {hours_per_month} hours monthly, what's your monthly salary? "))
gain_per_hour = monthly_salary / hours_per_month
print(f"You gain {gain_per_hour} reais per hour, considering you work 5x2 and gain {monthly_salary} reais per month")
