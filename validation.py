def get_input():
    while True:
        user_input = input("Enter a number between 1 and 10: ")
        try:
            number = int(user_input)
            if 1 <= number <= 10:
                return number
            else:
                print("Please enter a number between 1 and 10.")
        except ValueError:
            print("Invalid input. Please enter a valid number between 1 and 10.")

if __name__ == "__main__":
    result = get_input()
    print("You entered:", result)
