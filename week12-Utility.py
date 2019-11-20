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

#Define Function 5
def ScoreFinder(list_1, list_2, string):
    index_of_string = list_1.index(string)
    return index_of_string
    if index_of_string == True:
        print(f'OUTPUT {string} got a score of {list_2[index]}')
    else:
        print('OUTPUT player is not found')

#Define Function 6
def Union(list_1, list_2):
    new_list = []
    for i in list_1:
        if i not in new_list:
            new_list.append(i)
    for j in list_2:
        if j not in new_list:
            new_list.append(j)
    return new_list

#Define Function 7
def Intersection(list_1, list_2):
    intersected_list = []
    for i in list_1:
        if i in list_2:
            intersected_list.append(i)
    return intersected_list

#Define Function 8
def NotIn(list_1, list_2):
    not_in_list = []
    for i in list_1:
        if i not in list_2:
            not_in_list.append(i)
    return not_in_list




    
