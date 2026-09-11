import random as r

def main():
    alphabet  = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    first_char = r.choice(alphabet)
    second_char = r.choice(alphabet)
    num = r.randint(10000,99999)
    formattedplate = f"{second_char}{first_char}-{str(num)}"
    print(f"generated license plate: {formattedplate}")

if __name__ == "__main__":
    while True:
        quit = "Q"
        opt = input(f"please select number of times and {quit} to quit: ").upper()
        if opt.isdigit():
            for i in range(int(opt)):
                main()
        elif opt == quit:
            break
        else:
            print(f"error message: place an int value or {quit} to quit")
