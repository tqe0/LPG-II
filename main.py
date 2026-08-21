import random as r

def ascii():
    print("""$$$$$$$$$$$$$$$$$$$$$$$$$$$$@@@$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$@WbrxrfffjrrjrLMB@$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$@LvjffffjffjrJQ@@@@@$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$@BmczzzXXzzzzzcrjrjjL%@$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$@@$$$$%Qmqqq0XzzzzzzzzzzccvcvJ8$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$Mpbm#8LMMMMMMWMqXzzzzzzzzzzx@kvY@$$$$$$$$$$$$$$$$$$
$$$$$$$$@OkbkkZbWWWMMMMMMWoQzzzzzzzzzz*$8o$$$$$$$$$$$$$$$$$$
$$$$$$$@@dkkkkkbUuuvXaWWWMWWWqzzzzzzzzv>,`.$$$$$$$$$$$$$$$$$
$$$$$$$$@mkQkkkkkkkkkkpUUw*qxYwLzzzzzzzv>..f$$$$$$$$$$$$$$$$
$$$$$$$$$OkkZkkkkkkkkkkr!lir*[':~jnczzzzct`+$$$$$$$$$$$$$$$$
$$$$$$$$$#qkpwkqJf^.;(||\||\;|>.^`...I/jjj(jmQw%$$$$$$$$$$$$
$$$$$$$$$@abkd~......^l\||||!,:.-j ...`1\|)~bkbm@$$$$$$$$$$$
$$$$$$$$$$@(............<|||,...}kq:....:<~qwbkbM$$$$$$$$$$$
$$$$$$$$@UI....')x!.......~||1i.{bbkqwwjcqbkbkkb0$$$$$$$$$$$
$$$$$$@|.. -tYubbbk<....... (|+;bbbbZbbM0bkkkkkkka@$$$$$$$$$
$$$$$$$a...@0zXvYbkkq_.......?ObbbbmdbbB8qbkkkkkkk@$$$$$$$$$
$$$$$$$$$X0$bruXXzrwbkkkkbkkkkkkkkkkL@@$$@qkkkkkkpM@$$$$$$$$
$$$$$$$$$$$$@JrnzYXXXuxUmkkkkbkdmObB$$$$$$@wbkkkkbm@$$$$$$$$
$$$$$$$$$$$$$$xxxnXXvCbkkkkbbbdbkQ@$$$$$$$$@kbkkkkkO$$$$$$$$
$$$$$$$$$$$$$@OrxrrxzYuYbkkkkkkkkkL@$$$@@MZkbkkkkkpq$$$$$$$$
$$$$$$$$$$$$$$$fjrrrrrxcvdkkkkkkkkbh@@kbdkkkkkbkkwB$$$$$$$$$
$$$$$$$$$$$$$$$b(]jrrrrrrrqkkkkkkkkmpkkkkkkkkbqq@$$$$$$$$$$$
$$$$$$$$$$$$&q&aQ\]{rrxnrrvpkkkkkkbkQbkkkkk0bM$$$$$$$$$$$$$$
$$$$$$$$$$$@okbLpw|][trLUnr0kkkkkkkkbJZpB@@$$$$$$$$$$$$$$$$$
$$$$$$$$$@hwOqkd0bQ\]]/vQbCvbkkbbkkkkdb@$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$@mkdqkkk0kZ/]]nOCkJbkkbqkkkkkw8$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$8Zbkpkm0ZOJ(]uCQbbkkkbqdkkkkm&$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$@B0kb0pkkbkCnqkkpmbkkkpmkkkkd8$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$WwCkkkkkkCLkbkqObkkkkwmkkbq8$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$BJmkkkkkbbkkkO0bkkkkkqmkbmZQk@$$$$$$$$$$$$$$$$$
$$$$$$$$$$@@bpkbZOwwwwqmQbkpOkkkkkbZpbQZmmmh@$$$$$$$$$$$$$$$
$$$$$$$$$$@*pkkkkkkkbkkkkkkkUbkkkkkbQ0ZmmmmZo$$$$$$$$$$$$$$$
$$$$$$$$$$@Jbkkkkkkkkkkkkkkkk0kkkkkkkLmmmmmmwB$$$$$$$$$$$$$$
""") # u can delete this if youd like
    print()

def main():
    alphabet  = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    first_char = r.choice(alphabet)
    second_char = r.choice(alphabet)
    num = r.randint(10000,99999)
    formattedplate = f"{second_char}{first_char}-{str(num)}"
    print(f"generated license plate: {formattedplate}")

if __name__ == "__main__":
    ascii()
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
