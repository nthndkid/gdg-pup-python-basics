
# Part 1: For Loop - Printing a list of favorite foods
favorite_foods = ['Dinakdakan', 'Sisig', 'Adobo', 'Kare-Kare', 'Menudo']

# loop to print each food in the list
print("Here are my favorite foods:")
for food in favorite_foods:
    print(f"- {food}")  # display each food from the list


print("\n") 

# Part 2: While Loop - Countdown from a number
try:
    start_num = int(input("Enter a positive number to start the countdown: "))

    # if num is positive
    if start_num <= 0:
        print("Invalid input: Please enter a number greater than zero.")
    else:
        print("Countdown:")
        # loop through starting number up to 1
        while start_num > 0:
            print(start_num) # display current num
            start_num -= 1   # Reduce the number by 1

        print("Countdown complete!")  # output message after countdown
except ValueError:
    print("Invalid input: Please enter a valid number.")