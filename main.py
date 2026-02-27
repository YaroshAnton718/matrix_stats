from utils import *

def main():
    """
    The main function. Prints the result.
    """
    array = []
    random_elements(array)

    pos_elem = search_element(array)
    mean_val = mean_elements(array)

    print(f"The mean of elements above secondary diagonal: {round(mean_val, 2)}")

    if pos_elem > mean_val:
        print("The first positive element is greater than mean of elements above secondary diagonal.")
    elif pos_elem < mean_val:
        print("The first positive element is less than mean of elements above secondary diagonal.")
    else:
        print("The first positive element and mean of elements above secondary diagonal are equal.")

if "__main__" == __name__:
    main()