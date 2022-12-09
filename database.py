'''
database.py
Hang (Elia) Phan
@eliahangphan
12/09/2022

------------------------------------
This file contains the Database class.
------------------------------------
'''


import csv


class Database:
    def __init__(self, csvfilename = None):
        '''Initializes Database object with empty fields. If csv file is given as parameter, read the file.'''
        self.data_dict = {} # a dictionary of database
        self.horizontal = [] # a list of the database dictionary values
        self.vertical = [] # a list of the database dictionary keys
        self.vertical_pos = [] # a list of the database dictionary positive values
        self.vertical_neg = [] # a list of the database dictionary negative values
        self.data1 = {} # a dictionary containing the first third of data_dict
        self.data2 = {} # a dictionary containing the second third of data_dict
        self.data3 = {} # a dictionary containing the last third of data_dict
        if csvfilename != None:
            self.read(csvfilename)

    def get_data(self): 
        '''Access the dictionary of data.'''
        return self.data_dict

    def get_horizontal(self):
        '''Access the list of keys of the dictionary of data 
        (which is horizontal value of the graph).'''
        return self.horizontal

    def get_vertical(self):
        '''Access the list of values of the dictionary of data 
        (which is vertical value of the graph).'''
        return self.vertical

    def set_vertical(self, vertical):
        '''Mutate the list of values of the dictionary of data 
        (which is vertical value of the graph).'''
        self.vertical = vertical

    def set_horizontal(self, horizontal):
        '''Mutate the list of keys of the dictionary of data 
        (which is horizontal value of the graph).'''
        self.horizontal = horizontal

    def read(self, csvfilename):
        '''Reads a csv. file and create data_dict, horizontal, vertical, vertical_pos, vertical_neg from read information.'''
        data_dict = {}
        with open (csvfilename, 'r') as database: 
            read_database = csv.DictReader(database) #DictReader() returns a list of dictionaries 
        
            #Maps information in all dictionaries into one dictionary
            for line in read_database:
                new_key = int(line['Year'])
                new_value = float(line['Value'])
                data_dict[new_key] = new_value

        #Adds data_dict
        self.data_dict = data_dict

        #Adds horizontal
        self.vertical = list(self.data_dict.values())

        #Adds vertical
        self.horizontal = list(self.data_dict.keys())

        #Add vertical_pos
        vertical_pos = self.vertical[:]
        for i in self.vertical:
            if i < 0:
                vertical_pos.remove(i)
        self.vertical_pos = vertical_pos

        #Add vertical_neg
        vertical_neg = self.vertical[:]
        for i in self.vertical:
            if i > 0:
                vertical_neg.remove(i)
        self.vertical_neg = vertical_neg

        #Split data_dict into three dictionaries and add data1, data2, data3
        sub_length = int(len(self.horizontal)/3) # sub_length is an estimate of the length of data1, data2, data3

        for i in self.horizontal[:sub_length]:
            self.data1[i] = self.data_dict[i]
        for i in self.horizontal[sub_length:sub_length*2]:
            self.data2[i] = self.data_dict[i]
        for i in self.horizontal[sub_length*2:]:
            self.data3[i] = self.data_dict[i]


def test():
    '''Test function for the Database Class.'''
    data = Database('1880-2022.csv')
    #print(data.data_dict)
    #print(data.vertical)
    #print(data.horizontal)
    #print(data.vertical_neg)
    #print(data.vertical_pos)
    print(data.data1)
    #print(data.data2)
    #print(data.data3)    
    
if __name__ == "__main__":
    test()