# 아래 클래스를 수정하시오.
class StringRepeater:
    def __init__(self):
        pass

    def repeat_string(self, n, s):
        self.n = n
        self.s = s
        for i in range(self.n):
            print(s)


repeater1 = StringRepeater()
repeater1.repeat_string(3, "Hello")
