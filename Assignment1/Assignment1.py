# -*- coding: utf-8 -*-
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


def extract_username(userName):
    '''
    This function introduces Eliza to the User, asks the User their name and begins the conversation.
    '''
    userName = input('Hello, my name is Eliza. I am a psychotherapist. What is your name? \n'.upper()).strip().lower().strip(punctuation)
    userName,userNameIsGood = check_valid_user_name(userName) #true or false

    while not(userNameIsGood): #until we have a good user name
        userName = input("I'm sorry I didn't catch that. What is your name again? \n").strip().lower().strip(punctuation).upper()
        userName, userNameIsGood = check_valid_user_name(userName)


    print(('Nice to meet you, ' + userName + ". ").upper())
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
    should say in response. The function takes the user's response, filters
    the text through various analyzers and determines what response should be
    provided to the user. Bulk of program is provided here.
    '''
    repetitionList =['Can you repeat that, ' + userName.upper() + '? \n', "I'm not sure I follow? \n",
                     "I didn't quite understand, can you say that another way? \n",]

    def transform(Input):
		#Replace "i" with "you"
        output = re.sub(r'\bi\b',r'-1-',Input)

		#Replace "am" with "are"
        output = re.sub(r'\bam\b',r'-2-',output)

		#Replace "my" with "your"
        output = re.sub(r"\bmy\b",r'-3-',output)

		#Replace "was" with "were"
        output = re.sub(r"\bwas\b",r'-4-',output)

		#Replace "me" with "you"
        output = re.sub(r"\bme\b",r'-5-',output)

		#Replace "mine" with "yours"
        output = re.sub(r"\bmine\b",r'-6-',output)

		#Replace "you" with "I"
        output = re.sub(r"\byou\b",r'-7-',output)

		#Replace "your" with "my"
        output = re.sub(r"\byour\b",r'-8-',output)

		#Replace "yours" with "mine"
        output = re.sub(r"\byours\b",r'-9-',output)

		#Replace "are" with "am"
        output = re.sub(r"\bare\b",r'-10-',output)

		#Replace "were" with "was"
        output = re.sub(r"\bwere\b",r'-11-',output)

        output = re.sub(r'-1-',r'you',output)
        output = re.sub(r'-2-',r'are',output)
        output = re.sub(r"-3-",r'your',output)
        output = re.sub(r"-4-",r'were',output)
        output = re.sub(r"-5-",r'you',output)
        output = re.sub(r"-6-",r'yours',output)
        output = re.sub(r"-7-",r'I',output)
        output = re.sub(r"-8-",r'my',output)
        output = re.sub(r"-9-",r'mine',output)
        output = re.sub(r"-10-",r'am',output)
        output = re.sub(r"-11-",r'was',output)

        return output

    #If block to search for inputs starting with "how"
    if re.search(r"^(how) (.*)",userInput):
        #Reply is selected from this list
        howRepliesList = ['What do you think?', 'Why do you ask?',]
        output = random.choice(howRepliesList)
        return output.upper() + '\n', True

    #If block to search for inputs starting with "Can you"
    if re.search(r"^can you.*",userInput):
        #Partition the input to find the context of it
        before, mid, after = userInput.partition('can you')
        #Reply is selected from this list
        canRepliesList = ['Sure','What made you think I can' + after + '?']
        output = random.choice(canRepliesList)
        return output + '\n', True

    #If block to search for inputs starting with "Can I"
    if re.search(r"^can i.*",userInput):
        #Partition the input to find the context of it
        before, mid, after = userInput.partition('can i')
        #Reply is selected from this list
        canRepliesList = ['Sure','What made you think you can' + after + '?']
        output = random.choice(canRepliesList)
        return output + '\n', True

    #If block to search for inputs starting with "Who"
    if re.search(r"^who.*",userInput):
        return "Who do you think?".upper() + '\n', True

    #If block to search for inputs starting with "Hi or Hello"
    if re.search(r"\b(hi|hello)\b",userInput):
        return "Hello again. What's on your mind?".upper() + '\n', True

    #If block to search for inputs having "all" in the sentence
    if re.search(r".* all .*",userInput):
        return "In what way?".upper() + '\n', True

    #If block to search for inputs having "always" in the sentence
    if re.search(r".* always .*",userInput):
        return "Can you think of a specific example?".upper()+ '\n', True

    #If block to search for inputs having the keyword "depressed/sad/upset" and sending reply based on it
    if re.search(r"\b(depressed|sad|upset)\b",userInput):
        output = re.sub(r".*\b(depressed|sad|upset)\b.*",
               r"What made you \1? \n",userInput)
        return output.upper(), True

    #If block to search for inputs having "yes or no" in the sentence
    if re.search(r"\b(yes|no)\b",userInput):
        return "And why do you think that is?".upper() + '\n', True

    #If block to search for inputs having "gave me" in the sentence
    if re.search(r"\b(gave) me\b",userInput):
        output = re.sub(r".*\b(gave)\b.*",
               r"What made them give you that?",userInput)
        return output.upper(), True

	#Good bye list
    if re.search(r"\b(bye|farewell|adios)\b",userInput):
        return "\n", False

    # if there is no match ask them the question:
    else:
       #Get the transformed text by changing "You to I" or "am to are"
       transformed_text = transform(userInput).upper()
       return transformed_text.upper() + '? \n', True
	'''
       #Created lambda function for asking default questions to the user
       mylist = defaultdict(lambda: 'Why ')
       mylist['I AM'] = 'Why are you'
       mylist['YOU ARE'] = 'Why do you think you are'

       if re.search(r"^i am.*",userInput):
            append_word = mylist['I AM']
            before, mid, after = transformed_text.partition('YOU ARE')
            output =  userName + ', ' + append_word + after
       elif re.search(r"^you are.*",userInput):
            append_word = mylist['YOU ARE']
            print(transformed_text)
            before, mid, after = transformed_text.partition('I AM')
            output =  userName + ', ' + append_word + after
       else:
            append_word = mylist['default']
            output =  userName + ', ' + append_word + transformed_text

       return output.upper() + '? \n', True
    '''


def main():
    '''
    This is the main function. Conversation is started.
    conversation is continued until an ending is reached. The conversation is ended.
    '''
    #Variable Initialization
    converse = True
    userName = ""
    misundestandingCounter=0

	#Eliza will introduce from one of the replies from this introduction list
    introductionList =['What is on your mind today? \n', 'How do you feel today? \n',]

	#Eliza will end the conversation with his statement
    goodbyeList =['I hope this conversation was productive. Goodbye. \n','Goodbye. \n', 'Farewell \n',]

    print(eliza)

    #main function:
	# start conversation and get user's name
    userName = extract_username(userName)

	#initiate conversation dialogue, choose from introduction list
    userInput = input(random.choice(introductionList).upper()).strip().strip(punctuation).lower()

	#while conversation continues:
    while converse:
        reply, converse = determine_reply(userInput, userName) #determine a reply based on user input and if conversation should continue
        if converse:
            userInput = input(reply).strip().strip(punctuation).lower() #if there is a reply allow user to respond

	#say goodbye if user types bye or farewell or adios
    print(random.choice(goodbyeList).upper())


if __name__ == '__main__':
    main()
