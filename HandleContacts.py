'''
Created on Aug 14, 2014

@author: Max Ruiz
'''



from tkinter import *
cntcts = "Contacts.txt"

def createContact(cInstance):
    cont = open(cntcts, 'a')
    cont.write(cInstance.returnContaceInfoString())
    cont.close()



def assembleContacts():
    cList = []
    w = 20
    header = '|' + 'First Name'.ljust(w) + '|' + 'Last Name'.ljust(w) + '|' + 'Email'.ljust(w) + '|' + 'Phone Number'.ljust(w) + '|' + 'Address'.ljust(w)
    with open(cntcts, 'r') as cont:
        for line in cont:
            cList.append(line)
    tp = Toplevel(None, width = 100)
    lf = LabelFrame(tp, text="Contacts")
    lb0 = Listbox(lf)

    lf.pack(fill = 'both')
    lb0.insert(0, header)
    for j in range(len(cList)):
        lb0.insert(j+1, cList[j])
    lb0.pack(fill = 'both')
