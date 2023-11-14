
rapierDmg = (2,6)

def main():
    print(DmgAvr(rapierDmg))

def DmgAvr(wepDmg):
    dmgchance = []
    dieCount = []
    for i in range(0,wepDmg[1]):
            dmgchance.append(i+1)
    if wepDmg[0] == 1:
        return sum(dmgchance)/len(dmgchance)
    else:
        for i in range(0,wepDmg[0]):
            dieCount.append(dmgchance)
        dieOp = dieOptions(dieCount)
        return dieCount

def dieOptions(dieArray,):
    pass

def dieRollOp(size):
    lst = []
    for options in range(1,size+1):
        lst.append(options)
    return lst

if __name__ == "__main__":
    main()