'''
lsystem.py
Hang (Elia) Phan
@eliahangphan
12/09/2022

------------------------------------
This file contains the Lsystem class.
------------------------------------
'''

import tkinter as tk


class Lsystem:
    def __init__(self, filename = None):
        '''Initializes Lsystem object with empty base and rules field'''
        self.base = ''
        self.rules = []
        if filename != None:		
            self.read(filename)


    def setBase(self, b): 
        '''Sets lsystem base'''
        self.base = b


    def addRule(self, newrule): 
        '''Adds new rule to lsystem rules field'''
        self.rules.append(newrule)


    def replace(self, istring):
        '''Creates lsystem string'''
        tstring = ''
        for c in istring:
            found = False
            for rule in self.rules:
                if rule[0] == c:
                    tstring += rule[1]
                    found = True
                    break
            if found == False:
                tstring += c
        return tstring


    def read(self, filename):
        '''Opens/reads file and creates lsystem rules and base'''
        self.rules = []
        fp = open(filename, "r")
        for line in fp:
            line = line.strip()
            words = line.split(' ')
            if words[0] == 'base':
                Lsystem.setBase(self, words[1])
            elif words[0] == 'rule':
                Lsystem.addRule(self, words[1:])
        fp.close()


    def buildString(self, iterations):
        '''Creates lsystem string with certain number of iterations'''
        nstring = self.base
        for i in range(iterations): 
            nstring = self.replace(nstring)  
        return nstring