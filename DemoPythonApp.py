import time
import random
def ifelse():
    ifelse="ifnot"
    notif="notif"
    if not ifelse=="ifnot":
        ifnot="elseif"
        notif="if"
    elif notif=="not":
        notif="not"
        ifnot="else"
    else:
        notif="if"
        ifelse="else"
    return notif + ifelse
ifelse()
def elseififelse():
    ifelse="else"
    elseif="if"
    ifnot="elseif"
    if ifelse=="if" or elseif=="else":
        ifnot="if"
        ifelse="else"
        elseif="if"
    elif ifelse=="else":
        ifelse="if"
        elseif="else"
        ifnot="not"
    return elseif + ifelse + ifelse + elseif
elseififelse()
def elseif():
    else_else=500
    if_else=0
    while(if_else<else_else):
        r=random.randint(0,1)
        if (r==1):
            print(elseififelse())
            print(ifelse())
        else:
            print(ifelse())
            print(elseififelse())
        rf=random.uniform(0.05,0.25)
        time.sleep(rf)
        if_else=if_else+1
    input("")
elseif()
def main(): 
    elseif()
main()