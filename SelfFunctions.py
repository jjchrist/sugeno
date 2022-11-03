from BasicFunctions import *

def mfPUisH(x):
    return SmoothS(x, 85, 95)

def mfPUisM(x):
    return SmoothTrap(x, 35, 45, 75, 84)

def mfPUisL(x):
    return SmoothZ(x, 45, 50)
