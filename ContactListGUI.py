'''
Created on Aug 14, 2014

@author: Max Ruiz
'''
from tkinter import *
import ContactClass as ccls
import handleContacts as hc

root = Tk()

def cutPaste(entry, lBox):
    lBox.insert(0, str(entry.get()))

def cutNoPaste(lBox):
    lBox.delete(0)

def documentContact(fN, lN, e, ph, ad):
    tempContact = ccls.Contact(fN.get(0), lN.get(0), e.get(0), ph.get(0), ad.get(0))
    hc.createContact(tempContact)

def addAllFields(a0, a1, a2, a3, a4, b0, b1, b2, b3, b4):
    cutPaste(a0, b0)
    cutPaste(a1, b1)
    cutPaste(a2, b2)
    cutPaste(a3, b3)
    cutPaste(a4, b4)

contactFrame = LabelFrame(root, text="Contact Info", bg = "cyan")
contactFrame.pack(side = 'top', fill = 'both')

'''================================================'''
fNameFrame = LabelFrame(contactFrame, text="First Name", bg = "cyan")
fNameLBox = Listbox(fNameFrame, height=1, cursor = "star")
fNameLBox.insert(0, 'N/A')
fNameEnter = Entry(fNameFrame)
fNameAdd = Button(fNameFrame, text="Add", command = lambda: cutPaste(fNameEnter, fNameLBox))
fNameDel = Button(fNameFrame, text="Delete", command = lambda: cutNoPaste(fNameLBox))
'''------------------------------------------------'''
fNameFrame.pack(side = 'left')
fNameLBox.pack(side = 'top')
fNameEnter.pack(side = 'top')
fNameAdd.pack(side = 'left')
fNameDel.pack(side = 'right')
'''================================================'''

'''================================================'''
lNameFrame = LabelFrame(contactFrame, text="Last Name", bg = "cyan")
lNameLBox = Listbox(lNameFrame, height=1, cursor = "star")
lNameLBox.insert(0, 'N/A')
lNameEnter = Entry(lNameFrame)
lNameAdd = Button(lNameFrame, text="Add", command = lambda: cutPaste(lNameEnter, lNameLBox))
lNameDel = Button(lNameFrame, text="Delete", command = lambda: cutNoPaste(lNameLBox))
'''------------------------------------------------'''
lNameFrame.pack(side = 'left')
lNameLBox.pack(side = 'top')
lNameEnter.pack(side = 'top')
lNameAdd.pack(side = 'left')
lNameDel.pack(side = 'right')
'''================================================'''

'''================================================'''
emailFrame = LabelFrame(contactFrame, text="Email", bg = "cyan")
emailLBox = Listbox(emailFrame, height=1, cursor = "star")
emailLBox.insert(0, 'N/A')
emailEnter = Entry(emailFrame)
emailAdd = Button(emailFrame, text="Add", command = lambda: cutPaste(emailEnter, emailLBox))
emailDel = Button(emailFrame, text="Delete", command = lambda: cutNoPaste(emailLBox))
'''------------------------------------------------'''
emailFrame.pack(side = 'left')
emailLBox.pack(side = 'top')
emailEnter.pack(side = 'top')
emailAdd.pack(side = 'left')
emailDel.pack(side = 'right')
'''================================================'''

'''================================================'''
phoneNumberFrame = LabelFrame(contactFrame, text="Phone Number", bg = "cyan")
phoneNumberLBox = Listbox(phoneNumberFrame, height=1, cursor = "star")
phoneNumberLBox.insert(0, 'N/A')
phoneNumberEnter = Entry(phoneNumberFrame)
phoneNumberAdd = Button(phoneNumberFrame, text="Add", command = lambda: cutPaste(phoneNumberEnter, phoneNumberLBox))
phoneNumberDel = Button(phoneNumberFrame, text="Delete", command = lambda: cutNoPaste(phoneNumberLBox))
'''------------------------------------------------'''
phoneNumberFrame.pack(side = 'left')
phoneNumberLBox.pack(side = 'top')
phoneNumberEnter.pack(side = 'top')
phoneNumberAdd.pack(side = 'left')
phoneNumberDel.pack(side = 'right')
'''================================================'''

'''================================================'''
addressFrame = LabelFrame(contactFrame, text="Address", bg = "cyan")
addressLBox = Listbox(addressFrame, height=1, cursor = "star")
addressLBox.insert(0, 'N/A')
addressEnter = Entry(addressFrame)
addressAdd = Button(addressFrame, text="Add", command = lambda: cutPaste(addressEnter, addressLBox))
addressDel = Button(addressFrame, text="Delete", command = lambda: cutNoPaste(addressLBox))
'''------------------------------------------------'''
addressFrame.pack(side = 'left')
addressLBox.pack(side = 'top')
addressEnter.pack(side = 'top')
addressAdd.pack(side = 'left')
addressDel.pack(side = 'right')
'''================================================'''

actionFrame = LabelFrame(root, text="Actions", bg = "cyan")
actionFrame.pack(fill = 'both')

addAll = Button(actionFrame, text="Add All", command = lambda: addAllFields(fNameEnter, lNameEnter, emailEnter, phoneNumberEnter, addressEnter, fNameLBox, lNameLBox, emailLBox, phoneNumberLBox, addressLBox))
addAll['bg'] = 'yellow'
addAll.pack(side = 'left')

saveContact = Button(actionFrame, text="save", command = lambda: documentContact(fNameLBox, lNameLBox, emailLBox, phoneNumberLBox, addressLBox))
saveContact['bg'] = 'green'
saveContact.pack(side = 'left')

displayContacts = Button(actionFrame, text = "Display Contacts", command = lambda: hc.assembleContacts(), bg='blue')
displayContacts.pack(side = 'left')

exit = Button(actionFrame, text = "Exit", bg = "red", command = sys.exit)
exit.pack(side = "right")

root.mainloop()


