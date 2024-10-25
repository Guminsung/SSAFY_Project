# 아래 함수를 수정하시오.
def difference_sets(st1,st2):
    st = st1.difference(st2)
    return st

result = difference_sets({1, 2, 3}, {3, 4, 5})
print(result)
