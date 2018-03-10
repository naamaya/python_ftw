def palindrome_tester(number):
    """
    Recieves a 6-digit number as input. Checks if it has a palindrome in its last 4 digits.
    If yes, checks if after adding 1, the result has a palindrome in its last 5 digts.
    If yes, checks if another addition of 1 results in a palindrome in the middle 4 digits.
    If yes, check if a final addition of 1 results in a 6-digit palindrome.
    Output is a logical- true if all conditions exist.
    :param number:
    :return:
    """
    num_str=str(number)
    if num_str[2]==num_str[5] and num_str[3]==num_str[4]:
        first_check=1
    else:
        first_check=0
        second_check=0
        third_check=0
        fourth_check=0

    if first_check==1:
        number=number+1
        num_str=str(number)
        if num_str[1]==num_str[5] and num_str[2]==num_str[4]:
            second_check=1
        else:
            second_check=0
            third_check = 0
            fourth_check = 0

    if second_check==1:
        number=number+1
        num_str=str(number)
        if num_str[1]==num_str[4] and num_str[2]==num_str[3]:
            third_check=1
        else:
            third_check=0
            fourth_check=0

    if third_check==1:
        number=number+1
        num_str=str(number)
        if num_str[0]==num_str[5] and num_str[1]==num_str[4] and num_str[2]==num_str[3]:
            fourth_check=1
        else:
            fourth_check=0

    if fourth_check==1:
        ans=True
    else:
        ans=False

    return ans


def check_palindrome():
    """
    Runs through all 6-digit numbers and checks the mentioned conditions.
    The function prints out the numbers that satisfy this condition.

    Note: It should print out the first number (with a palindrome in its last 4 digits),
    not all 4 "versions" of it.
    """

    palindromes=[]
    every_6dig_num=range(100000,999999)

    for number in every_6dig_num:
        if palindrome_tester(number)==1:
            palindromes.append(number)

    return palindromes
