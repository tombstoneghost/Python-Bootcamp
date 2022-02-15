# Greeting
print("Welcome to the tip calculator.")

# Total Bill
total_bill = float(input("What was the total bill? $"))

# Tip Percentage
tip_percent = int(input("What percentage tip would you lik to give? 10, 12, or 15? "))

# Number of People
no_people = int(input("How many people to split the bill? "))

# Calculate Tip
tip = (total_bill * tip_percent)/100

# Each Person Share
share = (total_bill + tip)/no_people

print("Each person should pay {:.2f}".format(share))
