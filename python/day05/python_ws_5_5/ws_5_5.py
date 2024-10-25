# 아래 함수를 수정하시오.
def even_elements(lst):
    new_list = []
    new_list.extend(lst)
    for i in new_list:
        if i % 2 == 1:
            new_list.pop(new_list.index(i))
    return new_list

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)
