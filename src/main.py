import config
import hunt
import coxinha


def main():
    cox = coxinha.Coxinha()

    if config.Config.hunt.lower() == "hunt":
        hunt.hunt()
    else:
        print(">>> Hunt not defined!")


if __name__ == '__main__':
    main()
