print ('welcome to Brooklyn-99 trivia')
print ('are you ready??')
print ('five questions to see if you really lnow brooklyn-99')
print ('if you get one wrong, you lose.')
print ('so be careful')
print ('question one:')
answer1= 'Sharon'
if answer1== input ('what is terrys wifes first name? (make sure to use a capital and spell the name correctly)'):
    print ('your right next question')
    answer2= 'Peralta'
    if answer2== input ('whats jakes last name? (use capitals and spell correctly'):
        print ('right again!!!')
        answer3= 'Charles'
        if answer3== input ('what is Boyles first name? (spelling and capitals)'):
            print ('your on fire!!') 
            answer4= 'Jimmy'
            if answer4== input ('name The Butcher Finguss last name. (spelling and Caps)'):
                print ('right again! last question:')
                answer5= 'watch'
                if answer5== input ('name the second thing that jake tried to steal in the halloween heist.(one word)'):
                    print('YOU WIN!!!!!!!!!!')    
                else:
                    print ('wrong. your out')
            else:
                print ('wrong. your out')
        else:
            print ('wrong. your out')
    else:
        print ('wrong. your out')
else:
    print ('wrong. your out')
       
     

       
        
