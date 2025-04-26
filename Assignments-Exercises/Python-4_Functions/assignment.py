def create_greeting(name):
    """
    Create a personalized greeting message.
    Parameters:
        name (str): The name to include in the greeting.
    Returns:
        str: The greeting message.
    """
    return (f"Hello {name}, welcome to the GDG Web Development Team! "
            "You're doing great, and I truly believe that someday you'll be an amazing developer."
            "Life may feel challenging right now, and programming can be overwhelming at times, but remember, all your hard work will pay off in the end. "
            "Keep pushing forward, you're on the right path!")

try:
    name = input("Enter your name: ")
    greeting = create_greeting(name)
    print(f"The greeting message is: {greeting}")

except ValueError:
    print("Invalid input: Please enter a valid name.")