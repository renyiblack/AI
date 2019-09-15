from src.hunt_low import *

'''
    This program is set to work on a 1366x768(16:9) display
'''


def main():
    hunt_param = "../txt/HuntParam.txt"

    '''
        settings: array that stores content from HuntParam.txt line by line
        settings[0]: Stores location name
        settings[1]: Stores initial marker
        settings[2]: Stores maximum number of marks
    '''

    try:
        print(">>> Opening source file...")
        print(">>> Getting hunt parameters...")
        with open(hunt_param) as param:
            settings = param.read().splitlines()

        #  print(">>> local = " + settings[0] + ", markers = " + settings[1] + ", max markers = " + settings[2])
    except IndexError:
        print(">>> Error! Change hunt params!")

    if settings[0] == "hunt low lvl":
        print(">>> Starting hunt low...")
        hunt_low(int(settings[1]), int(settings[2]))
    else:
        print(">>> Hunt not defined!")


if __name__ == '__main__':
    main()
