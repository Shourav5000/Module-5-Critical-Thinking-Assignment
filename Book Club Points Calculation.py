# Part 2: Book Club Points Calculation

# Ask the user to enter the number of books purchased
books_purchased = int(input("Enter the number of books purchased this month: "))

# Determine the number of points earned based on the number of books purchased
if books_purchased == 0:
    points = 0
elif books_purchased == 2:
    points = 5
elif books_purchased == 4:
    points = 15
elif books_purchased == 6:
    points = 30
elif books_purchased >= 8:
    points = 60
else:
    points = 0  # For any other cases, no points are awarded

# Display the number of points earned
print(f"You have earned {points} points this month.")
