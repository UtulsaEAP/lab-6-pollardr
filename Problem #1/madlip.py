def food_input():
    
    #type you while  loop here
    condition = False
    while not condition:
        user_input = input()
        tokens = user_input.split()

        if tokens[0].lower() == 'quit':
            condition = True
        else:
            print(f'Eating {tokens[1]} {tokens[0]} a day keeps you happy and healthy.')
    

if __name__ == "__main__":
    food_input()
