# AIT 690 | Assignment 1 | Due 9/19/2018
### Billy Ermlick
### Xiaojie Guo
### Nidhi Mehrotra
This code aims to implement a dialogue robot Eliza who can engage in a dialogue with the user.
Eliza will begin the dialogue by asking the name of the user. Current implementation of Eliza contains:
1)	"Word Spotting" function to extract the keywords from users' answer and give related feedback. (e.g. 'sad' to 'What makes you sad?')
2)	 Transforming Sentences from user to the answers/questions from Eliza.(e.g " I love you." to "You love me?")
3)	Personalized the conversation by using user name in some of the questions
4)	Robust answers in some plausible way when the users enters some gibberish sentence or the sentences are not understandable (e.g.I'm sorry I didn't catch that. What is your name again?
5)	Used lambda function for asking default questions to the user, such as storing and returning the user's favorite things throughout discourse.
HOW TO RUN THE PROGRAM:
When using the code, just run the Assignment1.py and type your response into the prompt and press ENTER. Do not use contractions.
***********************************************************************************
Simple Example Dialogue:
HELLO, MY NAME IS ELIZA. I AM A PSYCHOTHERAPIST. WHAT IS YOUR NAME?
    'My name is Coco'
NICE TO MEET YOU, COCO. HOW DO YOU FEEL TODAY? 
    'i fee l sAD...'    
"I DIDN'T QUITE UNDERSTAND. CAN YOU SAY THAT ANOTHER WAY?"
    'I feel sad'
TELL ME MORE.
    'I always have lot of work to do'
CAN YOU THINK OF A SPECIFIC EXAMPLE?
    'Yes, I need to read 10 paper a week'
ARE YOU SURE?
    'Pretty sure'
COCO, WHY PRETTY SURE?     
    'can you sing a song for me?'
Sure
    'I want to share my favorites'
COCO, WHY DO YOU WANT TO SHARE YOUR FAVORITES?    
    'favorite is an interesting topic'
SPEAKING OF FAVORITES... I'D LIKE TO LEARN MORE ABOUT YOU
I know your favorite song is ...well maybe I am not sure....
...What is your favorite song?  
    'My favorite song is Raise you up'   
GOT IT. WHAT ELSE IS ON YOUR MIND?     
    'Nothing! bye"
I HOPE THIS CONVERSATION WAS PRODUCTIVE. GOODBYE.
***************************************************************************************

