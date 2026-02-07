def fibonacci(n):
    # Requirement: A list named 'sequence' initialized with [0, 1]
    sequence = [0, 1]

    # Handle the base cases
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Dynamic programming: Build the sequence iteratively
    # We calculate every number from index 2 up to index n
    for i in range(2, n + 1):
        # Rule: sum of the two preceding numbers
        next_val = sequence[i - 1] + sequence[i - 2]
        sequence.append(next_val)

    # Return the n-th number
    return sequence[n]
