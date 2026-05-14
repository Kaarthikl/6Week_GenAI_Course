# Date and Time Operations in Python

from datetime import datetime, timedelta

# 1. Current Date and Time
now = datetime.now()

print("Current Date and Time:")
print(now)

# 2. Current Date
current_date = now.date()

print("\nCurrent Date:")
print(current_date)

# 3. Current Time
current_time = now.time()

print("\nCurrent Time:")
print(current_time)

# 4. Formatting Date and Time
formatted = now.strftime("%d-%m-%Y %H:%M:%S")

print("\nFormatted Date and Time:")
print(formatted)

# 5. Adding 5 Days
future_date = now + timedelta(days=5)

print("\nDate After 5 Days:")
print(future_date)

# 6. Difference Between Two Dates
date1 = datetime(2026, 5, 1)
date2 = datetime(2026, 5, 14)

difference = date2 - date1

print("\nDifference Between Dates:")
print(difference.days, "days")