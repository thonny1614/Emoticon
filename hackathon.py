import pandas as pd 
import matplotlib as mp
import random
import os
import string
import time
import sys

userpass = open("UsersandPasses.txt","r+")
lines = userpass.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].split()
accountinfo = []

commonpass = ["password","hello","admin","123456","12345678","123456789","welcome","Welcome","Password"]

def create_accountus():
    enterus = input("please enter a username: ")
    ok = True
    if " " in enterus:
        print("please enter a username without a space")
        ok = False

    for i in range(len(lines)):
        if enterus == lines[i][0]:
            print("username taken")
            ok = False
            break
    if ok == True:
        accountinfo.append(enterus)
        create_accountp()
        return None
    else:
        create_accountus()
            

def create_accountp():
    enterpass = input("please enter a password with at least 6 characters: ")
    ok = True
    if " " in enterpass:
        print("please enter a password without a space")
        ok = False
    elif enterpass in commonpass:
        print("this password is common, please enter a more secure password")
        ok = False
    elif len(enterpass) < 6:
        print("please enter a password that's at least 6 characters long")
        ok = False
    if ok == True:
        accountinfo.append(enterpass)
        create_accounts()
        return None
    else:
        create_accountp()

def create_accounts():
    whichone = input("Do you want to make a teacher account or student account (t for teacher, s for student): ")
    ok = True
    if whichone.upper() != "T" and whichone.upper() != "S":
        print("please enter a valid letter")
        ok = False
    if ok == True:
        accountinfo.append(whichone)
        if len(lines) == 0:
            accountinfo.append(0)
        else:
            accountinfo.append(str(int(lines[-1][3])+1))
        if len(lines) <= 1:
            userpass.write(str(accountinfo[0]) + " " + str(accountinfo[1]) + " " + str(accountinfo[2]) + " " + str(accountinfo[3]))
        else:
            userpass.write("\n" + str(accountinfo[0]) + " " + str(accountinfo[1]) + " " + str(accountinfo[2]) + " " + str(accountinfo[3]))
        close()
        if whichone.upper() == "T":
            teachmenu(accountinfo)
        else:
            studmenu(accountinfo)
        return None
    else:
        create_accounts()

def close():
    userpass.close()
    return None

def loginuser():
    userlog = input("What's your username?: ")
    currentaccount = 0
    for i in range(len(lines)):
        if userlog == lines[i][0]:
            currentaccount = i
            loginpass(currentaccount)
            return None
    print("username doesn't exist")
    loginuser()


def loginpass(account):

    passlog = input("What's your password?: ")
    if lines[account][1] == passlog:
        print("welcome")
        passinto = lines[account]
        close()
        if lines[account][2] == "t":
            teachmenu(passinto)
        else:
            studmenu(passinto)
        return None
    else:
        print("incorrect password")
        loginpass(account)


def joinclass(info):
    joinclass = open("classes.txt","r+")
    classes = joinclass.readlines()
    listofclass = []
    for i in range(len(classes)):
        listofclass.append(classes[i].split())
    print(listofclass)
    classcode = input("enter the code for the class you'd like to join: ")
    joined = 0
    for i in range(len(listofclass)):
        if listofclass[i][1] == classcode:
            joined = i
            print("class found")
            joinclass.close()
            with open('classes.txt', 'a') as file:
                file.seek(i * 256)
                file.write(' ' + info[3])
            studmenu(info)
            return None
    print("class not found")
    joinclass.close()
    joinclass(info)
        

def createclass(info):
    addclass = open("classes.txt","r+")
    existing = addclass.readlines()
    for i in range(len(existing)):
        existing[i] = existing[i].split()
    classn = input("Please enter a class name: ")
    for i in range(len(existing)):
        if classn == existing[i][0]:
            print("this class name is in use")
            createclass(info)
            return None
    if " " in classn:
        print("please enter a name without a space")
        createclass(info)
    else:

        letters = string.ascii_letters
        code = ''.join(random.choice(letters) for _ in range(6))
        #add


        if len(existing) <= 1:
            addclass.write(classn + " " + code + " " + str(info[3]))
        else:  
            addclass.write("\n" + classn + " " + code + " " + str(info[3]))
        
        print("Your class code is: " + code)
        addclass.close()
        classstr = classn + ".txt"
        newclass = open(classstr, "x")
        teachmenu(info)
        newclass.close()
        return None
        
def createassign(info):
    assignwhich = input("Assignments you could assign 1. Solving quadratics: ")
    if assignwhich == "1" or assignwhich == " 1 " or assignwhich == " 1" or assignwhich == "1 ":
        addassign = open("test.txt","r+")
        length = addassign.readlines()
        if len(length) <= 1:
            addassign.write("solvingquadratics.txt")
        else:
            addassign.write("\n" + "solvingquadratics.txt")
        addassign.close()
        teachmenu(info)
    else:
        print("Not a valid number")
        createassign(info)

def solvethis(info,level,point):
    problemset = open(level,"r")
    each = problemset.readlines()

    adjust = []
    for i in range(12):
        if i in [0,3,6,9]:
            subl = []
            tvars = each[i][:-1].split()
            subl.append(tvars[0])
            subl.append(tvars[1].split(","))
        else:
            subl.append(each[i][:-1])
            if i in [2,5,8,11]:
                adjust.append(subl)

    select = random.randint(0,3)

    print(adjust[select][0])
    answer = input("type answer here (type hint for hint), (note: if an answer is a decimal round the nearest hundreth, fractions not accepted), (seperate solutions by a space): ")
    if "hint" in answer:
        levelof = input("Do you want an l1 or l2 hint?: ")
        if "l1" in levelof:
            print(adjust[select][2])
            tryagain(info,level,adjust[select],point*0.75,False)
            return None
        else:
            print(adjust[select][3])
            tryagain(info,level,adjust[select],point*0.5,False)
            return None
    answer = answer.split()
    answer == answer.sort()
    if answer == adjust[select][1]:
        print("correct answer")
        print(str(point) + " points earned")
        addps = open("solvingquadratics.txt","r+")
        findkid = addps.readlines()
        for i in range(len(findkid)):
            if findkid[i].find(info[0]) != -1:

                
                if len(findkid) <= 1:
                    solvethis.write(info[0] + " " + point)
                else:
                    with open('solvingquadratics.txt', 'a') as file:
                        file.seek(i * 256)
                        file.write(" " + str(point))
                addps.close()
                solvethis(info,level,point)
                return None
    else:
        tryagain(info,level,adjust[select],point*0.5,True)
        return None
            

def tryagain(info,level,prob,left,wrong):
    if wrong == False:
        answerit = input("type answer here (type hint for hint), (note: if an answer is a decimal round the nearest hundreth, fractions not accepted): ")
        if "hint" in answerit:
            levelof = input("Do you want an l1 or l2 hint?: ")
            if "l1" in levelof:
                print(prob[2])
                tryagain(info,level,prob,left*0.75,False)
                return None
            else:
                print(prob[3])
                tryagain(info,level,prob,left*0.5,False)
                return None
        answerit = answerit.split()
        answerit == answerit.sort()
        if answerit == prob[1]:
            print("correct answer")
            print(str(left) + " points earned")
            solvethis(info,level,str(level)*100)
            addps = open("solvingquadratics.txt","r+")
            findkid = addps.readlines()
            for i in range(len(findkid)):
                if findkid[i].find(info[0]) != -1:
                    findkid[i]
                    if len(findkid) <= 1:
                        solvethis.write(info[0] + " " + left)
                    else:
                        with open('solvingquadratics.txt', 'a') as file:
                            file.seek(i * 256)
                            file.write(" " + str(left))
                    solvethis(info,level,int(level[-5])*100)
                    return None
        else:
            tryagain(info,level,prob,left*0.5,False)
            return None
    else: 
        print("answer incorrect")
        answerit = input("type answer here (type hint for hint), (note: if an answer is a decimal round the nearest hundreth, fractions not accepted): ")
        if "hint" in answerit:
            levelof = input("Do you want an l1 or l2 hint?: ")
            if "l1" in levelof:
                print(prob[2])
                tryagain(info,level,prob,left*0.75,False)
                return None
            else:
                print(prob[3])
                tryagain(info,level,prob,left*0.5,False)
                return None
        answerit = answerit.split()
        answerit == answerit.sort()
        if answerit == prob[1]:
            print("correct answer")
            print(str(left) + " points earned")
            addps = open("solvingquadratics.txt","r+")
            findkid = addps.readlines()
            for i in range(len(findkid)):
                if findkid[i].find(info[0]) != -1:
                    findkid[i]
                    if len(findkid) <= 1:
                        solvethis.write(info[0] + " " + left)
                    else:
                        with open('solvingquadratics.txt', 'a') as file:
                            file.seek(i * 256)
                            file.write(" " + str(left))
                    solvethis(info,level,int(level[-5])*100)
                    return None
        else:
            tryagain(info,level,prob,left*0.5,False)
            return None

def viewassigns(info):
    ok = True
    whichclassin = open("classes.txt","r")
    findit = whichclassin.readlines()
    theclass = []
    for i in range(len(findit)):
        theclass.append(findit[i].split())
    for i in range(len(findit)):
        if findit[i].find(str(info[3])) != -1:
           thefile = str(theclass[i][0]) + '.txt'
           whichclassin.close()
           theclass = open(thefile,"r")
           allassigns = theclass.readlines()
           available = ""
           for l in range(len(allassigns)):
                if allassigns[l].find(".txt"):
                    available += str(allassigns[l][:-4]) 
                    available += ", "
           print("assignments available are " + available + ":")
           theclass.close()
           option = input("Do you want to 1. complete an assignment 2. exit: ")
           if option == "1" or option == " 1 " or option == " 1" or option == "1 ":
                probs(info,"solvingquadratics.txt")
           elif option == "2" or option == " 2 " or option == " 2" or option == "2 ":
                studmenu(info)
        else:
            if i == len(findit)-1:
                ok = False
    if ok == False:    
        print("No assignments")
        whichclassin.close()
        studmenu(info)

def probs(info, toopen):
    type = input("Would you like to do 1. lv1, 2. lv2, 3. lv3 4. exit: ")
    if type == "1" or type == " 1 " or type == " 1" or type == "1 ":
        solvethis(info,"quadeqlv1.txt",100)
    elif type == "2" or type == " 2 " or type == " 2" or type == "2 ":
        solvethis(info,"quadeqlv2.txt",200)
    elif type == "3" or type == " 3 " or type == " 3" or type == "3 ":
        solvethis(info,"quadeqlv3.txt",300)
    elif type == "4" or type == " 4 " or type == " 4" or type == "4 ":
        sys.exit()
    else:
        print("Please type in a valid number")



def studmenu(info):
    
    actions = input("What would you like to do 1. join a class 2. view assignements 3. exit: ")
    if actions == "1" or actions == " 1 " or actions == " 1" or actions == "1 ":
        joinclass(info)

    elif actions == "2" or actions == " 2 " or actions == " 2" or actions == "2 ":
        viewassigns(info)
    elif actions == "3" or actions == " 3 " or actions == " 3" or actions == "3 ":
        sys.exit()
    else:
        print("please enter a valid number")
        studmenu(info)

def teachmenu(info):

    actions = input("What would you like to do 1. create a class 2. view assignments 3. create an assignment 4. view analytics 5. exit: ")
    if actions == "1" or actions == " 1 " or actions == " 1" or actions == "1 ":
        createclass(info)

    elif actions == "2" or actions == " 2 " or actions == " 2" or actions == "2 ":
        pass
    elif actions == "3" or actions == " 3 " or actions == " 3" or actions == "3 ":
        createassign(info)
    elif actions == "4" or actions == " 4 " or actions == " 4" or actions == "4 ":
        pass
    elif actions == "5" or actions == " 5 " or actions == " 5" or actions == "5 ":
        sys.exit()
    else:
        print("please enter a valid number")
        teachmenu(info)
        

def greeting():
    enter = input("Hello, do you want to sign in or make a new account? (s for sign in and n for make a new account): ")
    if enter.lower() == "s":
        loginuser()
    elif enter.lower() == "n":
        create_accountus()
    else:
        print("please enter a valid character")
        greeting()
    

greeting()









    

