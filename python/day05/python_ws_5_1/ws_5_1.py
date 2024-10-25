# 아래 함수를 수정하시오.
def reverse_string(word):
    reverse_word = list(reversed(word))
    result = ''.join(reverse_word)
    return result

result = reverse_string("Hello, World!")
print(result)  # !dlroW ,olleH
