###################################
###################################
# © Copyright Pete Hewage 2019 ###
##################################
# Chat Application ###############
##################################














# Imports
import random





# temporary database
data = {'key':'value',
        "who are you?":'I am a cool chatbot, I shall attempt to answer your questions, but if I cant, ill let you teach me!',
        "who are you":'I am a cool chatbot, I shall attempt to answer your questions, but if I cant, ill let you teach me!'}







#loop
while True:
    
    
    #function to teach the application
    def teach():
        print('teach me something')
        question = input('What is the query?\n')
        answer = input('Okay, and what is the answer?\n')
        data[question] = answer
        print('Thank you!')
        read()


        
        
    #main function, starts the converstaion    
    def read():
        
        #different starters
        convo_beginner = 'Hi!'
        convo_determiner = random.randint(1,5)
        if convo_determiner == 1:
            convo_beginner = 'Hi! nice to see you! fire your questions away!\n'
        elif convo_determiner == 2:
            convo_beginner = 'Hi again!! Do you have a question?\n'
        elif convo_determiner == 3:
            convo_beginner = 'Greetings! Wanna talk? Ask me a question\n'
        elif convo_determiner == 4:
            convo_beginner = 'Hõla! How are you doing? Ask me a q!\n'
        elif convo_determiner == 5:
            convo_beginner = 'Hi, Whats up? ask me a question!\n'
        
        
        
        
        
        #bulk of the code
        read_val = input(convo_beginner)
        print()
        print()
        if read_val == 'teach':
            teach()
        else:
            try:
                print()
                print(data[read_val])
                print()
            except:
                print('Sorry, i dont know that one!')
                print()
                can_teach = input('can you teach me that one?')
                print()
                if can_teach == 'yes' or can_teach == 'Yes' or can_teach == 'Okay' or can_teach == 'okay' or can_teach == 'yep':
                    print('Great! Thanks!')
                    print()
                    print()
                    print()
                    teach()
                else:
                    print('okay then')
                    print()
                    read()
            
            
        
        
    #initialiser    
    read()