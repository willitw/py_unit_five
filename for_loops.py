def count(start, end):
    result = ""

    if start <= end:
        for num in range(start, end + 1):
            result += str(num) + " "
    else:
        for num in range(start, end - 1, -1):
            result += str(num) + " "

    return result

# Tests
print(count(0, 6))  # Output: "0 1 2 3 4 5 6 "
print(count(6, 0))  # Output: "6 5 4 3 2 1 0 "
