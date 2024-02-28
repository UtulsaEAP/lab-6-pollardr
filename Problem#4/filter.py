#Riley Pollard
# Lab thursday 2pm, Wednesday Class

def process_and_print(input_string):
      # Split into separate strings
    input_list = input_string.split()
    # Convert strings to integers and filter out negative values
    input_data = []
    for num in input_list:
        if int(num) <0:
            input_data.append(int(num))
    

    # Sort integers in reverse order
    input_data.sort(reverse=True)
  
    # Print sorted integers

    result = ''
    for num in input_data:
        result+= str(num) + ' '
    print(result)

if __name__ == "__main__":
    # User inputs string w/ numbers
    user_input = input("Enter a space-separated string of numbers: ")

    # Call the function to process and print the result
    process_and_print(user_input)
