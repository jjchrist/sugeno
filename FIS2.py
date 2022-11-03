from SelfFunctions import *

Purity = Height = Price = 0
A_PUisH = A_PUisM = A_PUisL = 0
PUisH = PUisM = PUisL = PR_PUisH = PR_PUisM = PR_PUisL = 0

def Fuzzyfication():
    global Purity
    global PUisE, PUisH, PUisM, PUisL

    PUisH = mfPUisH(Purity)
    PUisM = mfPUisM(Purity)
    PUisL = mfPUisL(Purity)


def FuzzyInference():
    global A_PUisH, A_PUisM, A_PUisL, PUisH, PUisM,  PUisL

    A_PUisH = PUisH
    A_PUisM = PUisM
    A_PUisL = PUisL
    

def Composition():
    global PR_PUisH, PR_PUisM, PR_PUisL
    global Height
    
    PR_PUisH = 150 * Height
    PR_PUisM = 100 * Height
    PR_PUisL = 10 * Height


def Defuzzyfication():
    global Price
    global A_PUisH, A_PUisM, A_PUisL,PR_PUisH, PR_PUisM, PR_PUisL

    Price = (A_PUisH * PR_PUisH + A_PUisM * PR_PUisM + A_PUisL * PR_PUisL)/(A_PUisH + A_PUisM + A_PUisL)

def Run():
    Fuzzyfication()
    FuzzyInference()
    Composition()
    Defuzzyfication()

def Init():
    global Purity, Height
    
    Purity = float(input('Purity = '))
    Height = float(input('Height = '))

def Terminate():
    global Price

    print('Price = ', Price)

def Main():
    print('Sugeno system')
    Init()
    Run()
    Terminate()

if __name__=='__main__':
    Main()






    












    
