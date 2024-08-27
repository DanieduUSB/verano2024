import time
import random as rnd

# Ciclo versión #1

"""hello = "hello world"
alfabet = "abcdefghijklmnopqrstuvwxyz"

random = rnd.sample(alfabet, 1)

string = ""

for letter in hello:
	if letter == " ":
		string = string + " "
		print(string)
	else:
		while letter != random[0]:
			print(string + random[0])
			random = rnd.sample(alfabet, 1)
			time.sleep(0.0125)
		
		string = string + random[0]
		print(string)
		random = rnd.sample(alfabet, 1)
		time.sleep(0.0125)"""

# Ciclo versión #2

"""hello = "hello world"
alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

string = ""

for letter in hello:
    
    rnd.shuffle(alph)
    
    if letter == " ":
        string = string + " "
        print (string)
        time.sleep(0.0125)
    else:
        for i in range(0, len(alph)):
            if alph[i] == letter:
                string = string + letter
                print(string)
                time.sleep(0.05)
                break
            else:
                print(string + alph[i])
                time.sleep(0.05)"""

# Ciclo versión #3

hello = "hello world"
alph = "abcdefghijklmnopqrstuvwxyz"

string = ""

for letter in hello:
    if letter == " ":
        string = string + " "
        print(string)
        time.sleep(0.05)
    else:
        for i in range(1,31):
            char = rnd.sample(alph, 1)
            if i == 30:
                string = string + letter
                print(string)
                time.sleep(0.05)
            elif char[0] == letter:
                string = string + char[0]
                print(string)
                time.sleep(0.05)
                break
            else:
                print(string + char[0])
                time.sleep(0.05)