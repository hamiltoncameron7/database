def Search():
    NP = input("Search by Name(N) or Phone Number(P)")
    Doc = open("db.txt", "r")
    found = False
    lineNum = 0
    if NP == 'P' or NP == 'p':
        Num = input("Enter the number (No spaces, parentheses or dashes): ")
        while found == False:
            line = Doc.readline()
            lineNum += 1
            print(line , ":")
            if str(line) == str(Num):
                print(line , " : " , Doc.readline())
                found = True
                return lineNum
    elif NP == 'N' or NP == 'n':
         Name = input("Enter the first and last names: ")
         last = Doc.readline()
         lineNum += 1
         while found == False:
             line = Doc.readline()
             if line == Name:
                 print(line , " : ", last)
                 found = True
                 return lineNum
             else:
                 lineNum += 1

def Append():
    N = input("Enter the first and last names: ")
    P = input("Enter the phone number (No spaces, parentheses or dashes): ")
    Doc = open("db.txt", "a")
    Doc.write(P + "\n")
    Doc.write(N + "\n")
    print("Added entry!")

def Delete():
    Lines = []
    Docu = open("db.txt", "r")
    for x in Docu:
        Lines.append(x)
    lineNum = Search()
    Lines[lineNum - 1] = ""
    Lines[lineNum] = ""
    Doc = open("db.txt", "w")
    Doc.writelines(Lines)

SAD = input("Search(S), Append(A), or Delete(D) entries from the database?")
if SAD == 'S' or SAD == 's':
    Search()
elif SAD == 'A' or SAD == 'a':
    Append()
elif SAD == 'D' or SAD == 'd':
    Delete()
