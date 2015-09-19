def stripKB():

    # Odstrani presledke in/ali vejice na koncu KB.

    new_line = ""
    
    f = open("KB.txt", "r")
    lines = f.readlines()
    for line in lines:
        if ", " in line[-3:-1]:
            new_line += line[:-3] + "\n"
        elif ", " in line[-2:]:
            new_line += line[:-2] + "\n"
        elif "," in line[-2]:
            new_line += line[:-2] + "\n"
        elif "," in line[-1]:
            new_line += line[:-1] + "\n"
        elif " " in line[-2]:
            new_line += line[:-2] + "\n"
        elif " " in line[-1]:
            new_line += line[:-1] + "\n"
        else:
            new_line += line
    f.close()

    f = open("KB.txt", "w")
    f.write(new_line)
    f.close()


def phraseMatch():

    # Doda "" na začetek in konec KB; KB morajo biti v vrsticah in brez presledkov in vejic na koncu.
    
    new_line = ""

    f = open("KB.txt", "r")
    lines = f.readlines()
    for line in lines:
        if "\n" in line:
            new_line += "\"" + line[:-1] + "\"\n"
        else:
            new_line += "\"" + line + "\""
    f.close()

    f = open("KB.txt", "w")
    f.write(new_line)
    f.close()


def stripPhrase():
    
    # Odstrani "" iz KB; KB morajo biti v vrsticah.
    
    new_line = ""

    f = open("KB.txt", "r")
    lines = f.readlines()
    for line in lines:
        if "\"" in line:
            new_line += line.replace("\"", "")
        else:
            new_line += line
    f.close()

    f = open("KB.txt", "w")
    f.write(new_line)
    f.close()


def exactMatch():

    # Doda [] na začetek in konec KB; KB morajo biti v vrsticah in brez presledkov in vejic na koncu.
    
    new_line = ""

    f = open("KB.txt", "r")
    lines = f.readlines()
    for line in lines:
        if "\n" in line:
            new_line += "[" + line[:-1] + "]\n"
        else:
            new_line += "[" + line + "]"
    f.close()

    f = open("KB.txt", "w")
    f.write(new_line)
    f.close()


def stripExact():
    
    # Odstrani [] iz KB; KB morajo biti v vrsticah.

    temp_line = ""
    new_line = ""

    f = open("KB.txt", "r")
    lines = f.readlines()
    for line in lines:
        if "[" in line:
            temp_line += line.replace("[", "")
        else:
            temp_line += line
    for line in temp_line:
        if "]" in line:
            new_line += line.replace("]", "")
        else:
            new_line += line
    f.close()

    f = open("KB.txt", "w")
    f.write(new_line)
    f.close()
    

def broadMatch():

    # Doda + na začetek KB; KB morajo biti v vrsticah.
    
    new_line = ""

    f = open("KB.txt", "r")
    lines = f.readlines()
    for line in lines:
        new_line += "+" + line
    f.close()

    f = open("KB.txt", "w")
    f.write(new_line)
    f.close()


def stripBroad():
    
    # Odstrani + izpred KB; KB morajo biti v vrsticah.
    
    new_line = ""

    f = open("KB.txt", "r")
    lines = f.readlines()
    for line in lines:
        if "+" in line[0]:
            new_line += line.replace("+", "")
        else:
            new_line += line
    f.close()

    f = open("KB.txt", "w")
    f.write(new_line)
    f.close()


def negativeMatch():
    
    # Doda - na začetek KB; KB morajo biti v vrsticah.
    
    new_line = ""

    f = open("KB.txt", "r")
    lines = f.readlines()
    for line in lines:
        new_line += "-" + line
    f.close()

    f = open("KB.txt", "w")
    f.write(new_line)
    f.close()


def stripNegative():
    
    # Odstrani - izpred KB; KB morajo biti v vrsticah.
    
    new_line = ""

    f = open("KB.txt", "r")
    lines = f.readlines()
    for line in lines:
        if "-" in line[0]:
            new_line += line.replace("-", "")
        else:
            new_line += line
    f.close()

    f = open("KB.txt", "w")
    f.write(new_line)
    f.close()
