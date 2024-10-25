# 아래 함수를 수정하시오.
def find_min_max(lst):
    new_list = sorted(lst)
    min_list = new_list[0]
    max_list = new_list[len(new_list) - 1]
    return (min_list, max_list)

result = find_min_max([3, 1, 7, 2, 5])
print(result)  # (1, 7)
