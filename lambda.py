data = [10, 501, 22, 37, 100, 999, 87, 351, 'Hello']  # Define a list containing integers and strings

# Check if every element is an integer or string
result = all(map(lambda x: isinstance(x, (int, str)), data))  # Check if each element is an instance of int or str using a lambda function

if result:
    print("All elements are integers or strings.")  # Print if all elements are integers or strings
else:
    print("Not all elements are integers or strings.")  # Print if not all elements are integers or strings

