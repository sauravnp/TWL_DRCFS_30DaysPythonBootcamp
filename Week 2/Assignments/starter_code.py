# Feel free to add as much lines as you want between ## START CODE HERE and ## END CODE HERE.
# Please donot write code outside this boundry or you may fail the test.

# start by importing the necessary documents

import random
import string 

def rank(pwd: str) -> str:
    '''
    Ranker function that ranks the password based on the assigned criteria

    Input: pwd -> character or string

    The following are the requirements for POOR / MODERATE / STRONG password.

    Passwords can contain (not required) any of the following requirements:  
    i. Lower case letters (a – z).       iii) Numbers ( 0 – 9 ).  
    ii. Upper case letters (A – Z).      iv) Symbols ( ! + - = ? # % * @ & ^ $ _ )

    1. A POOR Password is defined as: 
    a. Contains less than 3 from the above 4 items ( i – iv ).  
    b. Less than 8 characters in length.

    2. A MODERATE Password is defined as:  
    a. Contains 3 from the above 4 items ( i – iv )  
    b. Between 8 to 10 characters in length.

    3. A STRONG Password is defined as:  
    a. Meets all 4 of the above items ( i – iv )  
    b. Greater than 10 characters in length.

    Returns: rank -> rank of password; POOR / MODERATE / STRONG
    '''
    ## Start code here
    pass_rank = [0,0,0,0]
    Ualphabets = string.ascii_uppercase
    Lalphabets = string.ascii_lowercase
    chars =  "!+-=?#%*@&^$_"
    digits = string.digits
    for p in pwd:
        if p in Ualphabets :
            pass_rank[0] = 1
        elif p in Lalphabets:
            pass_rank[1] = 1
        elif p in digits:
             pass_rank[2] = 1
        elif p in chars:
             pass_rank[3] = 1
    strength = sum(pass_rank)
    if strength == 4 and len(pwd) > 10:
        return "STRONG"

    elif strength == 3 and (len(pwd) >= 8 and len(pwd) <= 10):
        return "MODERATE"

    elif strength < 3 and (len(pwd) < 8):
        return "WEAK"
    ## End code here
    return rank

def option1():
    '''
    Helper function that will be executed when user selects option 1 in the initial case.
    '''
    # Steps to follow:
    # 1. Ask user to rank password from either Users-Pwds.txt or a custom file (second part for bonus only you can skip this)
    # 2. Open the file containing username and password in each line and a file to store the ranked password information(Users-Pwds-Chked.txt).
    # 2.1 ## !IMPORTANT ## Store the list of username,passwords in a variable called usrpwds. 
    # 3. Use the rank() function to rank the password
    # 4. Write to the Users-Pwds-Chked.txt file (username,password,rank) in each line as string. Omit the brackets and only fill up the actual values. 
    # 5. Close necessary files and print to terminal.
    
    ## START CODE HERE
    usrpwds = 0
    file = input("Enter the user_pwds file name")
    with open(file, 'r') as contents ,open("Users.txt", 'a') as writefile:
        for content in contents:
                username, password = content.split(",")
                password = password.rstrip()
                strength = rank(password)
                writefile.write(f"{username},{password},{strength}")
                writefile.write("\n")
                usrpwds+=1
    ## END CODE HERE

    print('#'*80)
    # [INFO] Be sure to change userpwds with the name of variable that you give to the list of passwords
    print('[INFO] '+'Number of passwords checked:',str(usrpwds))
    print('[INFO] '+'The given rankings can be found in Users-Pwds-Chked.txt')
    print('#'*80)

def option2():
    '''
    Function to be executed when the user selects option 2 (generate password) in the main loop.
    
    Steps to follow:
        Prompt the user for a username (No more the 20 characters in length).
        Create a Function that will have no (zero) arguments. (generate)
        The Function will randomly generate a STRONG password (Meeting the STRONG Requirments).
        Ask the user if they would like this saved (Y or N).
        If Y: Open the Input file (Users-Pwds.txt) and append the username,password to the EOF.
        If N: Ask if they would like to generate a different password for this user (Y or N).
        Then the program loops back to the menu again offering displaying and offering to select 1, 2 or 3.
    '''

    def generate() -> str:
        '''
        Helper function to generate password.
        Returns: A string pwd with strong ranking in our ranking system.
        '''
        # Starter code, Ualphabets contains all upper case alphabets
        # Lalphabets condains all lowercase alphabets
        # chars contains all special characters and digits contains all numeric digits
        Ualphabets = string.ascii_uppercase
        Lalphabets = string.ascii_lowercase
        chars = string.punctuation
        digits = string.digits
        pwd = ''
        # Hint: user random.choice to select a random Upperalphabet(Ualphabet), Lalphabet, chars, and digits. Join then all together in pwd and check ranking
        # While the required ranking is not met continue joining new Ualphabet, Lalphabet, chars and digits.
        
        ## START CODE HERE
        while len(pwd) <=10:
            pwd += random.choice(Ualphabets) + random.choice(Lalphabets) + random.choice(chars) + random.choice(digits)

        ## END CODE HERE
        return pwd
    
    # Ask for username and check 20 character limits

    ## START CODE HERE
    while True:
        username = input("Enter the username you want to. It cannot  be more than length 20: ")
        if len(username) <= 20:
            break
    ## END CODE HERE

    # Generate the password using generate() and follow the steps as guided in the function header. 
    ## START CODE HERE
    while True:
        password = generate()
        choice = input("Password has been generated. Do you like this information to be saved? ")
        if choice == "Y":
            with open("Final-Users-Pwds(10).txt", "a") as file:
                file.write(f"{username},{password}")
                file.write("\n")
                break
        if choice == "N":
            choice = input("Would you like to generate a different password for this user?")
            if choice == "Y":
                pass
            if choice == "N":
                break
    ## END CODE HERE

def main():

    print('Welcome to my password ranking program')
    while True:
        print('-'*40)
        print('Please select one of 3 options')
        print('option1. Rank password from an existing file \t option2. Generate a strong password \noption3. exit the program')
        inp = input("Enter your option here:")
        
        # try converting the inp to integer form and then check condition if input was either option1, 2, 3 or something else. 
        # exit the loop by using the break command if the user selects 3 other wise use option1() and option 2() function 

        ## START CODE HERE
        inpt = int(inp)
        if inpt == 1:
            option1()
        if inpt == 2:
            option2()
        if inpt == 3:
            print("This program is courtesy of: Saurav")
            break
        ## END CODE HERE


# DONOT TOUCH THESE LINES
if __name__=='__main__':
    main()