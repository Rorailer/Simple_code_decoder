from random import choice
from string import ascii_letters

#What does the User want to do?
while True:
    question = input('Code or Decode? (c/d): ')
    
    print(question)
    if question[0] == 'c':
        coding = True
        print("Coding")
        break
    elif question[0] == 'd':
        coding = False
        print('Decoding')
        break
    else:
        print("Invalid Input!")    


#Taking the input(message)
message= input('Enter you message : ')

#Splitting sentance into words.
words = message.split(" ")

#Coding
if(coding):
    nwwords = []
    for word in words:
        if((len(word))>=3):
            s1 = "".join(choice(ascii_letters) for i in range(3))
            s2 = "".join(choice(ascii_letters) for i in range(3))
            nwword= s1 + word[1:]+ word[0] + s2
            nwwords.append(nwword)
        
        else:
            nwword= word[::-1]
            nwwords.append(nwword)
            
                        
    print(" ".join(nwwords))

#Decoding 
else:
    nwwords = []
    for word in words:
        if(len(word)>=3):
            nword = word[3:len(word)-3]
            # print('removeing random : '+nword)
            nword =  nword[-1] +  nword[0:len(nword)-1]
            # print(nword[0:len(nword)-1])
            nwwords.append(nword)    
        else:
            nword= word[::-1]
            nwwords.append(nword)
    print(" ".join(nwwords))        
