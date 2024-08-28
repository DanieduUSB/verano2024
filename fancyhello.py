import os 
import time
import random as rnd

hello = "hello world"
alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
rndchars = "!#$%&/()='[]+*´¨'¿?¡_-:.;,ñÑ<>/ÂÊ^ÎÔÛâêîôûàèìòùÀÈÌÒÙ~áéíóúαβγδεzηθιkλμνξoπρσςτυφχψωΓΔΘΛΞΠΣΦΨΩ"

k1 = 6
k2 = 5
string = ""

for letter in hello:

    rnd.shuffle(alph)
    rhello = ""
    rworld = ""

    if k1 == 0:
        k2 -= 1
    else:
        k1 -= 1
    
    if letter == " ":

        string = string + " "
        os.system('cls')
        print (string + "ûθ/¿Ê")
        k1 = 0
        time.sleep(0.040)

    else:
        for i in range(0, len(alph)):
            if alph[i] == letter:

                string = string + letter

                if k1 > 0:
                    rhello = ""
                    for j in range(0,k1 - 1):
                        rndhello = rnd.sample(rndchars,1)
                        rhello = rhello + rndhello[0]
                    
                    rworld = ""
                    for j in range(0,5):
                        rndworld = rnd.sample(rndchars,1)
                        rworld = rworld + rndworld[0]
                    
                    os.system('cls')
                    print(string + rhello + " " + rworld)
                
                else:
                    rworld = ""
                    for j in range(0,k2):
                        rndworld = rnd.sample(rndchars,1)
                        rworld = rworld + rndworld[0]
                
                    os.system('cls')
                    print(string + rworld)

                time.sleep(0.035)
                break
    
            else:

                if k1 > 0:

                    rhello = ""
                    for j in range(0,k1 - 1):
                        rndhello = rnd.sample(rndchars,1)
                        rhello = rhello + rndhello[0]
                    
                    rworld = ""
                    for j in range(0,5):
                        rndworld = rnd.sample(rndchars,1)
                        rworld = rworld + rndworld[0]
                    
                    os.system('cls')
                    print(string + alph[i] + rhello + " " + rworld)
                
                else:
                    rworld = ""
                    for j in range(0,k2):
                        rndworld = rnd.sample(rndchars,1)
                        rworld = rworld + rndworld[0]
                    
                    os.system('cls')
                    print(string + alph[i] + rworld)

                time.sleep(0.035)