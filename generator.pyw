import random
import tkinter as tk
from tkinter import ttk

## selsects a random index in password string that can be edited
def selectIndex(pwList, nonEditable):
    i = random.randint(0, len(pwList)-1)
    while (i in nonEditable):
        i = random.randint(0, len(pwList)-1)
    return i

## edits the password to match the selected attributes
def editValues(pwList, toEdit, nonEditable): # toEdit = [special, uppercase, lowercase, number]
    if (toEdit[0]):
        i = selectIndex(pwList, nonEditable)
        nonEditable.append(i)
        value = random.randint(33, 64)
        if(value > 60):
            value += 62
        elif(value > 54):
            value += 36
        elif(value > 47):
            value += 10
        pwList[i] = value
    if (toEdit[1]):
        i = selectIndex(pwList, nonEditable)
        nonEditable.append(i)
        value = random.randint(65, 90)
        pwList[i] = value
    if (toEdit[2]):
        i = selectIndex(pwList, nonEditable)
        nonEditable.append(i)
        value = random.randint(97, 122)
        pwList[i] = value
    if (toEdit[3]):
        i = selectIndex(pwList, nonEditable)
        value = random.randint(48, 57)
        pwList[i] = value
    return pwList

## returns the index of the first instance of the attr (False) or return the len list + 1 (True)
def needsEditing(pwList, ranges): 
    for i in range(len(pwList)):
        for j in range(len(ranges)//2):
            if (pwList[i] >= ranges[j*2] and pwList[i] <= ranges[j*2+1]):
                return i
            j += 1
    return len(pwList)+1

## verifes that the passowrd matches the attributes
def verify(pwList, attr): # attr = [pwLen, special, uppercase, lowercase, number]   
    nonEditable = []
    toEdit = [False, False, False, False] # toEdit = [special, uppercase, lowercase, number]  
    if (attr[1]):
        index = needsEditing(pwList, [33,47,58,64,91,96,123,126])
        toEdit[0] = bool(index-len(pwList)+1)
        if(not toEdit[0]):
            nonEditable.append(index)
    if (attr[2]):
        index = needsEditing(pwList, [65, 90])
        toEdit[1] = bool(index-len(pwList)+1)
        if(not toEdit[1]):
            nonEditable.append(index)
    if (attr[3]):
        index = needsEditing(pwList, [97, 122])
        toEdit[2] = bool(index-len(pwList)+1)
        if(not toEdit[2]):
            nonEditable.append(index)
    if (attr[4]):
        index = needsEditing(pwList, [48, 57])
        toEdit[3] = bool(index-len(pwList)+1)
        if(not toEdit[3]):
            nonEditable.append(index)
    return editValues(pwList, toEdit, nonEditable)

## generates a random password that has the attributes selected
def generate(attr): # attr = [pwLen, special, uppercase, lowercase, number]      
    pwList = []
    for i in range(attr[0]):
        rn = random.randint(33, 126)
        pwList.append(rn)

    # for i in range(1, len(attr)):
    #     if attr[i] == 'F':
    #         attr[i] = False
    #     else:
    #         attr[i] = True
    pwList = verify(pwList, attr)
    password = ""
    for i in pwList:
        password += chr(i)
    return password

#################
#################
#### Tkinter ####
#################
#################

## selection window
selectionWindow = tk.Tk()
selectionWindow.geometry("450x450")
selectionWindow.title("Password Generator Generator")

## on/off toggle variable
specCheckVar = tk.IntVar()
upperCheckVar = tk.IntVar()
lowerCheckVar = tk.IntVar()
numCheckVar = tk.IntVar()

## Check buttons and text entry for password attributes
lenEntry = ttk.Entry(selectionWindow, width = 50)
lenEntry.insert(0, "Length of the password (type a number from 4-20)")
specCheck = ttk.Checkbutton(selectionWindow, text = "Special Character", variable = specCheckVar, onvalue = 1, offvalue = 0, width = 20)
upperCheck = ttk.Checkbutton(selectionWindow, text = "Uppercase Character", variable = upperCheckVar, onvalue = 1, offvalue = 0, width = 20)
lowerCheck = ttk.Checkbutton(selectionWindow, text = "Lowercase Character", variable = lowerCheckVar, onvalue = 1, offvalue = 0, width = 20)
numCheck = ttk.Checkbutton(selectionWindow, text = "Number", variable = numCheckVar, onvalue = 1, offvalue = 0, width = 20)
passwordEntry = ttk.Entry(selectionWindow, text = "", foreground="green")

## button for generating password
generateRandomPasswordButton = ttk.Button(selectionWindow, text = "Generate Random Password", command = lambda: generatePassword())

## packs the selectionWindow buttons
def packSelectionButtons():
    lenEntry.pack()
    specCheck.pack()
    upperCheck.pack()
    lowerCheck.pack()
    numCheck.pack()
    generateRandomPasswordButton.pack()

## gets the data from the checkbuttons and entry
def getData(): 
    attr = []
    attr.append(int(lenEntry.get()))
    attr.append(bool(specCheckVar.get()))
    attr.append(bool(upperCheckVar.get()))
    attr.append(bool(lowerCheckVar.get()))
    attr.append(bool(numCheckVar.get()))
    return attr

## displays the password
def displayPassword(password):
    passwordEntry.config(text = password)
    passwordEntry.insert(0, password)
    passwordEntry.pack()

## collects attr data, generates password, displays password
def generatePassword():
    attr = getData()
    displayPassword(generate(attr))

## packs the selection window buttons and starts the selection window
packSelectionButtons()
selectionWindow.mainloop()

##starts the program
if __name__ == "__main__":
    selectionWindow.mainloop()
