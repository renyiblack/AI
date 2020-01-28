from config import Config
from hunt import hunt


def main():
    if Config.hunt.lower() == "hunt":
        hunt()
    else:
        print(">>> Hunt not defined!")


if __name__ == '__main__':
    main()
