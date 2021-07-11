import math 
list_in = []
a = 1
def bubble_sort_upside_down(vector):
    condition = True
    while condition:
        condition = False
        for i in range(len(vector) - 1):
            if vector[i] > vector[i + 1]:
                vector[i], vector[i + 1] = vector[i + 1], vector[i]
                condition = True
    return vector

def is_prime_basic(number):
    for value in range(2,int(math.sqrt(number))+1):
        if number % value == 0:
            return False
    return True


with open('filesname.txt') as flow:
    list_file_name = flow.readlines()
    txt_file_name = ''.join(list_file_name)
    delete_enter = txt_file_name.replace('\n', ' ')
    list_number = list(delete_enter.split(' '))

for i in range(len(list_number)-1):
    check = is_prime_basic(int(list_number[i]))
    if check == True:
        list_number[i] = list_in.append(list_number[i])
        print("Numbers are detected:")
        print(a)
        a = a+1
new_list_number = bubble_sort_upside_down(list_in)
new_string_number = " ".join(new_list_number)
print(new_string_number)