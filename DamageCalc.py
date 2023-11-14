def main():
    dmg = int(input("Please provide an acceptable size for the damage die: "))
    size = int(input("Please provide how many dice will be rolled: "))
    wepDmgStart = (size,dmg)
    option = ""
    passed = False
    while option.upper() != "C" and option.upper() != "A" and option.upper() != "R":
        if passed == False:
            option = input("What would you like to do with this damage roll? \nResisted Damage (R), Critical Damage (C), or Average Damage(A)?")
            passed = True
        else:
            option = input("That was an invalid option, please select an appropriate option. \nResisted Damage (R), Critical Damage (C), or Average Damage(A)?")
    match option.upper():
        case "A":
            print(DmgAvr(wepDmgStart))
        case "C":
            print(DmgCrt(wepDmgStart))
        case "R":
            print(DmgRes(wepDmgStart))

def DmgAvr(wepDmg):
    return ((wepDmg[1]+1)/2)*wepDmg[0]

def DmgRes(wepDmg):
    return DmgAvr(wepDmg)/2

def DmgCrt(wepDmg):
    return DmgAvr(wepDmg)*2

if __name__ == "__main__":
    main()