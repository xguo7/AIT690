"""
AIT 690 | Assignment 1 | Due 9/19/2018
Billy Ermlick
Nidhi
Xiaojie Guo

Description here...
check out default dict...


Your program should engage in a dialogue with the user, with your program Eliza playing the role of a
psychotherapist. Your program should be able carry out "word spotting", that is it should recognize
certain key words and respond simply based on that word being present in the input. It should also be
able to transform certain simple sentence forms from statements (from the user) into questions (that
Eliza will ask). Also, try to personalize the dialogue by asking and using the user's name.

In addition, your program should be robust. If the user inputs gibberish or a very complicated question,
Eliza should respond in some plausible way (I didn't quite understand, can you say that another way,
etc.). “Word spotting”, sentence transformation, and robustness are the minimum requirements for
your code.

You can implement additional functionalities, inspired by the dialogues presented in
Weizenbaum paper. You may receive up to 1 bonus point max for any additional functionalities.
This program should rely heavily on the use of regular expressions, so please make sure to review
some introductory material in Learning Python, Programming Python, or some other source before
attempting this program.


Please comment your code. In particular, explain what words you are spotting for (and why) and what
statement forms you are converting into questions (and why). Also make sure you name, class, etc. is
clearly included in the comments.
It is fine to use a Python reference book for examples of loops, variables, etc., but your Eliza specific
code must be your own, and not taken from any other source (human, published, on the web, etc.)


"""
import re
import random
from collections import defaultdict
# pet = defaultdict(lambda: 'dog')
# pet['kai'] = 'snake'
# print(pet['kevin'])



def extract_username(userName):
    '''
    This function introduces Eliza to the User, asks the User their name and begins the conversation.
    '''
    userName = input('Hello, my name is Eliza 2.0. I am a psychotherapist. What is your name? ').strip().lower()
    userNameIsGood = check_user_name(userName) #true or false

    while not(userNameIsGood): #until we have a good user name
        userName = input("I'm sorry I didn't catch that. What is your name again? ").strip().lower()
        userNameIsGood = check_user_name(userName)

    print('Nice to meet you, ' + userName.capitalize() + ".")


def check_user_name(userName):
    '''
    This function checks if the user's inputted name is properly entered.
    '''
    if len(userName) <10:
        return True
    else:
        return False





def hold_conversation():
    '''
    This function describes the steps taken by Eliza while holding a conversation with the User. This is the bulk of the program...
    '''
    print('What is on your mind today?')
    stuff = input()
    print('How do you feel about that?')


    converse = False
    return converse




def say_goodbye():
    '''
    This function generates ways for Eliza to say good bye and selects one at random to say to the User.
    '''
    goodbyeList =['I hope this conversation was productive. Goodbye.','Goodbye.', 'Farewell']
    print(random.choice(goodbyeList))




def main(username, converse):
    '''
    This is the main function.
    '''
    extract_username(userName)
    while converse:
        converse = hold_conversation()
    say_goodbye()






if __name__ == '__main__':
    converse = True
    userName = ""
    main(userName, converse)
