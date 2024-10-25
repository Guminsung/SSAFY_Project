# 아래 함수를 수정하시오.
def union_sets(st1,st2):
    st = st1.union(st2) 
    return st

result = union_sets({1, 2, 3}, {3, 4, 5})
print(result)
