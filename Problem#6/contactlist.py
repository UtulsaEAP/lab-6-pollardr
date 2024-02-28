#Riley Pollard
# Lab thursday 2pm, Wednesday Class

def process_user_contacts(user_input):
    user_contacts = {}
    
 
    input_pairs = user_input.split()
    

    # Put word pairs into a dictionary
    for pair in input_pairs:
        name, phone = pair.split(',')
        user_contacts[name] = phone
    
    # Get contact name from input, output contact's phone number
    contact_name = input("Enter the contact name: ")
    if contact_name in user_contacts:
        print(user_contacts[contact_name])
    else:
        print('Contact not found.')
    
   
if __name__ == '__main__':
    # Get input for word pairs
    user_input = input("Enter word pairs (name, phone number): ")

    # Call the function to process user contacts
    process_user_contacts(user_input)
