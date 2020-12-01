from time import sleep

# command aliases
cmds = {
    "calcs": ["calcs", "calc", "cal", "calclist", "calcli", "calculations", "calculate"],
    "printfile" : ["printfile", "read", "print", "file", "readfile"],
    "slots": ["slots", "slot", "sl"],
    "help": ["help", "h", "?", "commands", "cmds", "commandlist", "commandli", "cmdlist", "cmdli", "info"],
    "exit": ["exit", "quit", "end"]
    }

# command descriptions
cmdesc = {
    "calcs": "This command prints the calculations' +, -, * and / ' between two numbers",
    "printfile" : "This command prints the content of a file with a given path",
    "slots": "You can play slots with this command (WIP)",
    "help": """This command shows the aliases of either all commands or
more detailed help on a single command, if you provide the name""",
    "egg": "No eggs. Don't look for them. There are no eggs",
    "exit": "Guess what this command does..."
    }

version = "'beta 1.2'"

bal = 1000


# typewriter effect
def typewrite(*value, delay=0.02, sep=" ", end="\n"):
    r"""typewrite(value, delay=0.02, sep=" ", end="\n")

Prints the given values with a delay between each character.
This creates a nice typewriter effect.

    value: the value you want to have typed out
    delay: the delay between each character in seconds, default: 0.02 seconds
    sep: string inserted between values, default: a space
    end: string appended after the last value, default: a newline"""

    for i in range(len(value)):
        for c in str(value[i]):
            sleep(delay)
            print(c, end="", flush=True)
        if i != len(value) -1:
            print(end=sep, flush=True)
    sleep(delay)
    print(end=end)



def cmdline():
    return input("> ").lower().strip()

def whatcmd(cmdstr):
    """Figure out what command was typed in cmdline"""
    if cmdstr is not "":
        args = cmdstr.split()
        cmd = args[0]
        
        # if cmd is in the list of x, run function for x
        if   cmd in cmds["calcs"]:    declicalcs(args)
        elif cmd in cmds["printfile"]: printfile(args)
        elif cmd in cmds["slots"]:         slots(args)
        elif cmd in cmds["help"]:           help(args)
        elif cmd in     ["egg"]:      (typewrite("I'm sorry, I don't know what you want. Try 'help'."), print("", end="> "), sleep(2), typewrite("\rMaybe I'll be a discord bot one day...", end=""), sleep(1), print("\r                                      \r", end=""), typewrite("...", delay=0.3, end=""), sleep(1), print("\r   \r", end=""), typewrite("WAIT THATS BAD...", end=""), sleep(1), print("\r                 \r", end=""), typewrite("or is it?", delay=0.1, end=""), sleep(1), print("\r         \r", end=""))
        elif cmd in cmds["exit"]:
            return (typewrite("Goodbye!", delay=0.1), sleep(1))

        else: 
            typewrite("I'm sorry, I don't know what you want. Try 'help'.")

    whatcmd(cmdline())



def declicalcs(args):
    if len(args) == 1:
        typewrite("Which numbers would you like to use?")
        (cmdline()).split().insert(0, "calcs")
    elif len(args) == 2:
        typewrite("You need to use two numbers.")
    else:
        try:
            listcalcs(int(args[1]),int(args[2]))
        except:
            try:
                listcalcs(float(args[1].replace(",", ".")), float(args[2].replace(",", ".")))
            except:
                typewrite("Invalid input")

def listcalcs(x, y):
    """Print a list of four calculations between two numbers which use the operators '+', '-', '*' and '/'"""
    print(x, "+", y, "=", round(x + y, 12))
    print(x, "-", y, "=", round(x - y, 12))
    print(x, "*", y, "=", round(x * y, 12))
    print(x, "/", y, "=", round(x / y, 12))
    print()



def printfile(args):
    # check if user specified a path, if not, ask
    try:
        args[1]
    except:
        typewrite("What is the Path to your file?")
        args.append(cmdline())

    print(args)
    path = " ".join(args[1:]).strip(" \"'")
    print(path)
    exts = ["csv", "txt"]
    if path.split(".")[-1] not in exts:
        print("""Please only""", " and ".join(exts), """files!
I have no Idea what harmful things could happen,
if the program tried to open other file types.""")
        return

    try:
        print("opening...")
        file = open(path, "r")
    except:
        print("something went wrong")

    if file.mode == "r":
        print("reading...")
        for line in file:
            print(line, end="")
        typewrite("That's it...", delay=0.05)
        typewrite("That's all it can do so far...")
    file.close()



def slots(args):
    global bal
    amt = None
    # check if user specified a second argument, if not, ask
    try:
        args[1]
    except:
        typewrite("How much credits would you like to use?")
        args.append(cmdline().split()[0])
    # check if amt can be an int. if True, assign the value to amt
    # don't if user doesn't have enough credits
    try:
        amt = int(args[1])
        if amt > bal:
            return typewrite("You don't have enough credits.")
    except:
        try:
            float(amt)
            return typewrite("Amount must be a whole number.")
        except:
            if args[1] in ["bal", "balance", "credits"]:
                return typewrite("Your balance:", bal)
            else:
                return typewrite("Amount is not a number.")
    from random import randint
    
    symbols = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "!", "$", "%", "&", "?", "#"]
    
    print("--- S - L - O - T - S ---\n")
    bal -= amt
    print("    ╔═══╤═══╤═══╗")
    for i in range(0, randint(12, 15)):
        a = b = c = symbols[randint(0, len(symbols)-1)]
        print("\r    ║", a, "│", b, "│", c, "║", end="")
        sleep(0.1)
    for i in range(0, randint(12, 15)):
        b = c = symbols[randint(0, len(symbols)-1)]
        print("\r    ║", a, "│", b, "│", c, "║", end="")
        sleep(0.1)
    for i in range(0, randint(12, 15)):
        c = symbols[randint(0, len(symbols)-1)]
        print("\r    ║", a, "│", b, "│", c, "║", end="")
        sleep(0.1)
    print("\n    ╚═══╧═══╧═══╝")
    sleep(1)

    if a == b and b == c:
        bal += amt*100
        typewrite("You spent", amt, "and won", amt*100, "!!!")
    elif a == b or a == c or b == c:
        bal += amt*3
        typewrite("You spent", amt, "and won", amt*3, "!", delay=0.03)

    else:
        typewrite("You spent", amt, "and lost everything.", delay=0.05)



def help(args):
    if len(args) == 1:
        print("--- H - E - L - P ---")
        sleep(0.1)
        print("Version:", version, end="\n\n")
        sleep(0.1)
        print("Here are all comands and their aliases:")
        sleep(0.1)
        print("     help:", cmds["help"])
        print("    calcs:", cmds["calcs"])
        print("printfile:", cmds["printfile"])
        print("    slots:", cmds["slots"])
        print("     exit:", cmds["exit"])
        print()
    elif args[1] in cmds["help"]:      helpdesc("help")
    elif args[1] in cmds["calcs"]:     helpdesc("calcs")
    elif args[1] in cmds["printfile"]: helpdesc("printfile")
    elif args[1] in cmds["slots"]:     helpdesc("slot")
    elif args[1] in     ["egg"]:       helpdesc("egg")
    elif args[1] in cmds["exit"]:      helpdesc("exit") 
    else:
        typewrite("This command does not exist")

def helpdesc(key):
    typewrite(cmdesc[key])
    if key in cmds:
        print("Aliases for this command:")
        print("   ", cmds[key])




# start the program
sleep(1)

typewrite("Hello.", delay=0.05, end=" ")
sleep(0.2)

typewrite("What would you like to do?")
sleep(0.2)

typewrite("Type 'help' for a list of commands.")

whatcmd(cmdline())
