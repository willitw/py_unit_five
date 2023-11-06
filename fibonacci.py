def fibonacci(x):
    if x <= 0:
        return []

    if x == 1:
        return [1]

    sequence = [1, 1]
    while len(sequence) < x:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)

    return sequence


def main():
    x = int(input("Enter the number of Fibonacci numbers to generate: "))

    if x <= 0:
        print("Please enter a positive integer.")
    else:
        result = fibonacci(x)
        print("The first", x, "Fibonacci numbers are:")
        print(result)


if __name__ == "__main__":
    main()
