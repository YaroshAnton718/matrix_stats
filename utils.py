import random

def random_elements(arr):
    """
    Generates a random matrix from 1 to 100 elements in rows and columns.
    Then prints this matrix.

    Parameters:
        arr (list): A list of elements
    """
    m = random.randint(1, 10)
    n = random.randint(1, 10)

    for i in range(m):
        row = []
        for j in range(n):
            row.append(round(random.uniform(-100, 100), 2))

        arr.append(row)

    for i in range(m):
        print(arr[i])

def search_element(arr):
    """
    Finds the first positive element, searching in columns.

    Parameters:
        arr (list): A list of elements

    Returns:
        float: The first positive element
    """
    m = len(arr)
    n = len(arr[0])
    for j in range(n):
        for i in range(m):
            if arr[i][j] > 0:
                print(f"The first positive element in column is {arr[i][j]}")
                print(f"Location of this element: row {i}, column {j}")

                return arr[i][j]

def mean_elements(arr):
    """
    Calculates the sum of all elements above the secondary diagonal.
    Calculates the mean of all elements above the secondary diagonal.

    Parameters:
        arr (list): A list of elements

    Returns:
        float: The mean of elements
        string: The message, if no elements were found
    """
    total = 0
    count = 0
    m = len(arr)
    n = len(arr[0])
    for i in range(m):
        for j in range(n):
            if i + j < n - 1:
                total += arr[i][j]
                count += 1

    if count == 0:
        return "No elements found."
    else:
        mean = total / count
        return mean