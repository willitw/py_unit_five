def multiplication_table(number):
    if not isinstance(number, int) or number < 1:
        return "Invalid input. Please provide a positive integer."

    table = [str(number * i) for i in range(1, 13)]
    return " ".join(table)


if __name__ == "__main__":
    number = 5
    result = multiplication_table(number)
    print(result)
