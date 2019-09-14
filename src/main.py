from hunts.hunt_low import *
from hunts.hunt_no_heal import *


def main():
    hunt_param = "../txt/HuntParam.txt"

    '''
        settings: array that stores content from HuntParam.txt line by line
        settings[0]: Stores location name
        settings[1]: Stores initial marker
        settings[2]: Stores maximum number of marks
        '''

    try:
        print(">>> opening source file...")
        print(">>> getting hunt parameters...")
        with open(hunt_param) as param:
            settings = param.read().splitlines()

        #  print(">>> local = " + settings[0] + ", markers = " + settings[1] + ", max markers = " + settings[2])
    except IndexError:
        print(">>> Error! Change hunt params!")

    if settings[0] == "hunt low lvl":
        print(">>> calculating HuntLow...")
        HuntLow(int(settings[1]), int(settings[2]))
    elif settings[0] == "hunt no heal":
        print(">>> calculating hunt no heal...")
        HuntNoHeal(int(settings[1]), int(settings[2]))


if __name__ == '__main__':
    main()
