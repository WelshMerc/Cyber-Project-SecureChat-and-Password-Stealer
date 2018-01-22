def combination(list_1, list_2):
    blank_list = []
    for i in (range(len(list_1))):
        blank_list.append(list_1[i])
        blank_list.append(list_2[i])
    return(blank_list)

def splitter(list_1, list_2, list_3):
    i = 0
    while i <= len(list(list_1)):
        list_2.append(list_1[i-2])
        list_3.append(list_1[i-1])
        i = i + 2




