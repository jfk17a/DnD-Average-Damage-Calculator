
rapierDmg = (3,6)

def main():
    print(DmgCrt(rapierDmg))

def DmgAvr(wepDmg):
    return ((wepDmg[1]+1)/2)*wepDmg[0]

def DmgRes(wepDmg):
    return DmgAvr(wepDmg)/2

def DmgCrt(wepDmg):
    return DmgAvr(wepDmg)*2

if __name__ == "__main__":
    main()