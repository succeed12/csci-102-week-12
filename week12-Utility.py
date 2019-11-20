# https://github.com/succeed12/csci-102-week-12.git
#Eshita Mittal
#CSCI 102 - Section E
#Python Lab 12 B

#Define Functtoin 1
def PrintOutput(string_name):
    print('OUTPUT ', string_name)

#Define Function 2
def LoadFile(string):
    with open(string) as file:
        lines = file.readlines()
    line_list = []
    for line in lines:
        line_list.append(line)
    print(f'OUTPUT {line_list}')




    
