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

#Define Function 3
def UpdateString(string, replace_string, num):
    listed_string = list(string)
    listed_string[num] = replace_string
    new_string = ''.join(listed_string)
    print(f'OUTPUT {new_string}')

#Define Function 4
def FindWordCount(list_1, string):
    stringed_list_1 = ''.join(list_1)
    counted_string = stringed_list.count(string)
    print(f'OUTPUT {counted_string}')




    
