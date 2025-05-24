import random
import string
length=int(input("Tell me your password length (8-12) : "))
if 13>length>7:
    character=input("Tell me characters type (letters,numbers,symbols or all) : ")
    if character=='letters':
        char=string.ascii_letters
        pass1=''.join(random.choice(char) for i in range(length))
        print("Your generated password is : ",pass1)
    elif character=='numbers':
        num=string.digits
        pass2=''.join(random.choice(num) for i in range(length))
        print("Your generated password is : ",pass2)
    elif character=='symbols':
        sym=string.punctuation
        pass3=''.join(random.choice(sym) for i in range(length))
        print("Your generated password is : ",pass3)
    elif character=='letters numbers' or character=='numbers letters':
        ln=string.digits+string.ascii_letters
        pass4=''.join(random.choice(ln) for i in range(length))
        print("Your generated password is : ",pass4)
    elif character=='letters symbols'or character=='symbols letters':
        ls=string.punctuation+string.ascii_letters
        pass5=''.join(random.choice(ls) for i in range(length))
        print("Your generated password is : ",pass5)
    elif character=='numbers symbols'or character=='symbols numbers':
        ns=string.digits+string.punctuation
        pass6=''.join(random.choice(ns) for i in range(length))
        print("Your generated password is : ",pass6)
    elif character=='all':
        all1=string.digits+string.punctuation+string.ascii_letters
        pass7=''.join(random.choice(all1) for i in range(length))
        print("Your generated password is : ",pass7)
else:
    print("Out of range!")    