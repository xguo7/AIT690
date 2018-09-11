# -*- coding: utf-8 -*-
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
from string import punctuation
import nltk


eliza = (" \
                ||||||||||||||||||||||||||||||||||||||||||||||||| \n \
                ************************************************* \n \
                ||||||||||   ||            ||||||||        |||    \n \
                ||           ||      ||         |||       || ||   \n \
                |||||||      ||               |||        ||   ||  \n \
                ||           ||      ||     |||         ||||||||| \n \
                ||||||||||   ||||||  ||   ||||||||     ||      || \n \
                ************************************************* \n \
                ||||||||||||||||||||||||||||||||||||||||||||||||| \n \
               \n")


# pet = defaultdict(lambda: 'dog')
# pet['kai'] = 'snake'
# print(pet['kevin'])

def extract_username(userName):
    '''
    This function introduces Eliza to the User, asks the User their name and begins the conversation.
    '''
    userName = input('Hello, my name is Eliza. I am a psychotherapist. What is your name? ').strip().lower().strip(punctuation)
    userName,userNameIsGood = check_valid_user_name(userName) #true or false

    while not(userNameIsGood): #until we have a good user name
        userName = input("I'm sorry I didn't catch that. What is your name again? ").strip().lower().strip(punctuation)
        userName, userNameIsGood = check_valid_user_name(userName)


    print('Nice to meet you, ' + userName.capitalize() + ".")
    return userName


def check_valid_user_name(userName):
    '''
    This function extracts the username from the response and checks if the
    user's inputted name is valid.
    '''
    if name_retrieval('is\s(.*)',userName):  # get the word after "is"
        name=name_retrieval('is\s(.*)',userName)
    elif name_retrieval('am\s(.*)',userName):   # get the word after "am"
        name=name_retrieval('am\s(.*)',userName)
    else:  # if neither of those words, just get the text
        name=userName.partition(' ')[0]
    #error checking:
    if len(name) >=10:
        return [], False
    return name, True

def name_retrieval(re_pattern,content):
    '''
    This function returns either the name of the user or false, indicating that the
    result is not present.
    '''
    query=re.compile(re_pattern,re.MULTILINE|re.DOTALL)
    if len(re.findall(query,content))>0:
        return re.findall(query,content)[0]
    else:
        return False


def determine_reply(userInput, userName):
    '''
    This function analyzes the users response and determines what Eliza
    should say in response. The funciton takes the user's response, filters
    the text through various analyzers and determines what response should be
    provided to the user. Bulk of program is provided here.
    '''
    repetitionList =['Can you repeat that, ' + userName.capitalize() + '? ', "I'm not sure I follow? ",
                     "I didn't quite understand, can you say that another way? ",]
    userInput = userInput.strip(punctuation)
    output = re.sub(r"\bI'm\b",r'you are',userInput)
    output = re.sub(r"\bI am\b",r'you are',output)
    output = re.sub(r'\bI\b',r'you',output)
    output = re.sub(r'\bam\b',r'are',output)
    output = re.sub(r"\bmy\b",r'your',output)
    output = re.sub(r"\bwas\b",r'were',output)
    output = re.sub(r"\bme\b",r'you',output)
    output = re.sub(r"\bmine\b",r'yours',output)



    if re.search(r"^([Hh]ow|[Ww]hat) (.*)",userInput):
        return "What do you think? ", True

    if re.search(r"\b(hi|hello)\b",userInput):
        return "Hello again. What's on your mind? ", True

    if re.search(r".* all .*",userInput):
        return "In what way? ", True

    if re.search(r".* always .*",userInput):
        return "Can you think of a specific example? ", True

    if re.search(r"\b(depressed|sad|upset)\b",userInput):
        output = re.sub(r".*\b(depressed|sad|upset)\b.*",
               r"What made you \1?",userInput)
        return output.capitalize(), True

    if re.search(r"\b(yes|no)",userInput):
        return "And why do you think that is? ", True

    if re.search(r"\b(bye|fairwell|adios)\b",userInput):
        return "", False

    if re.search(r"\b(gave) me\b",userInput):
        output = re.sub(r".*\b(give|gave)\b.*",
               r"What made them give you that? ",userInput)
        return output.capitalize(), True

    # if there is no match ask them to rephrase the question:
    return output.capitalize() + '? ', True
    # return random.choice(repetitionList), True





def main():
    '''
    This is the main function. Conversation is started.
    conversation is continued until an ending is reached. The conversation is ended.
    '''
    #Variable Initialization
    converse = True
    userName = ""
    misundestandingCounter=0
    introductionList =['What is on your mind today? ', 'How do you feel today? ',]
    goodbyeList =['I hope this conversation was productive. Goodbye.','Goodbye.', 'Farewell',]
    print(eliza)


    #main function:
    userName = extract_username(userName) # start conversation and get their name
    userInput = input(random.choice(introductionList)).strip() #initiate conversation dialogue
    while converse: #while conversation continues:
        reply, converse = determine_reply(userInput, userName) #determine a reply based on user input and if conversation should continue
        if converse:
            userInput = input(reply) #if there is a reply allow user to respond

    print(random.choice(goodbyeList)) #say goodbye


if __name__ == '__main__':
    main()
