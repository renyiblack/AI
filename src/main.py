from hunt import hunt


def main():
    hunt_param = "../txt/HuntParam.txt"

    '''
        settings: array that stores content from HuntParam.txt line by line
        settings[0]: Stores location name
        settings[1]: Stores initial marker
        settings[2]: Stores maximum number of marks
    '''

    try:
        # Getting hunt params
        with open(hunt_param) as param:
            settings = param.read().splitlines()

    except IndexError:
        print(">>> Error! Change hunt params!")

    # Starting hunt
    if settings[0] == "hunt":
        hunt(int(settings[1]), int(settings[2]))
    else:
        print(">>> Hunt not defined!")


if __name__ == '__main__':
    main()
