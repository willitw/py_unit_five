def main():
    total = 0
    count = 0

    while True:
        user_input = input("Enter an integer (or 'q' to quit and find the average): ")

        if user_input == 'q':
            break  # Exit the loop if the user enters 'q'

        try:
            number = int(user_input)
            total += number
            count += 1
        except ValueError:
            print("Invalid input. Please enter an integer.")

    if count > 0:
        average = total / count
        print("Average of the entered numbers:", average)
    else:
        print("No valid numbers entered.")


if __name__ == "__main__":
    main()
