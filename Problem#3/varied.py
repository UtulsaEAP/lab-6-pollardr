#Riley Pollard
# Lab thursday 2pm, Wednesday Class

def process_input(input_string):
      # Split into separate strings

    # Convert strings to floats
    
    nums = list(map(float,input_string.split()))

    maxval = max(nums)
    avg = sum(nums)/len(nums)
    

    # Get max and average
    
    return maxval, avg

if __name__ == "__main__":
    # User inputs string w/ numbers
    user_input = input("Enter a space-separated string of numbers: ")

    # Call the function and get the results
    max_value, average_value = process_input(user_input)

    print(f'Max Value: {max_value:.2f}')
    print(f'Average Value: {average_value:.2f}')
