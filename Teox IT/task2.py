'''
Write a Python for :-
Input: [1, 2, [3, 4], 5, [6], 7, [8, [9, 10]]]
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''

input_lst = [1, 2, [3, 4], 5, [6], 7, [8, [9, 10]]]
output_lst = []
def check_list(input_lst):
    for i in input_lst :
        if isinstance(i,list):
            check_list(i)
        else:
            output_lst.append(i) 
check_list(input_lst)
print(output_lst)