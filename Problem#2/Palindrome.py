def check_palindrome(user_input):
 #type your code here
    str1 = ''
    for x in range(len(user_input)-1, -1,-1):
        str1 += user_input[x]
    if str1 == user_input:
        print('palindrome: ' + user_input)
    else:
        print('not a palindrome: ' + user_input)
if __name__ == "__main__":
    user_input = input()
    check_palindrome(user_input)
