'''
Created on Aug 13, 2014

@author: Max Ruiz
'''

class Contact(object):
    '''
    classdocs
    '''


    def __init__(self, firstName, lastName, email, phoneNum, address):
        '''
        Constructor
        '''
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.phoneNum = phoneNum
        self.address = address
        self.detail = [self.firstName, self.lastName, self.email, self.phoneNum, self.address]

    def returnName(self):
        return self.firstName

    def returnContactInfoList(self):
        info = [self.firstName, self.lastName, self.email, self.phoneNum, self.address]
        return info

    def returnContaceInfoString(self):
        info = ""
        w = 20
        for j in range(len(self.detail)):
            info = info + '|' + self.detail[j].ljust(w)
        info = info + '\n'
        return info

