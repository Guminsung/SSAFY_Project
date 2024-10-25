# 아래 함수를 수정하시오.
def count_character(text, char):
    num = text.count(char)
    return num

result = count_character("Hello, World!", "o")
print(result)  # 2
