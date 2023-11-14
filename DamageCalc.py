
rapierDmg = (2,6)

def main():
    print(DmgAvr(rapierDmg))
    # print(CrtDmgAvr(rapierDmg))
    # print(ResDmgAvr(rapierDmg))
    
def CrtDmgAvr(wepDmg):
    count, size = wepDmg
    count += count
    dmgChance = []
    for rolls in range(1,count+1):
        for options in range(1,size+1):
            # print("Die:", rolls)
            # print("Roll:",options)
            dmgChance.append(options)
    avg = sum(dmgChance)/len(dmgChance)
    return avg

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

def ResDmgAvr(wepDmg):
    count, size = wepDmg
    dmgChance = []
    for rolls in range(1,count+1):
        dmgChance.append(dieRollOp(size))
    dmgLst = []
    
    # avg = sum(dmgChance)/len(dmgChance)
    # avgRes = avg/2
    return dmgLst

def dieOptions(dieArray,):
    pass

def dieRollOp(size):
    lst = []
    for options in range(1,size+1):
        lst.append(options)
    return lst

if __name__ == "__main__":
    main()