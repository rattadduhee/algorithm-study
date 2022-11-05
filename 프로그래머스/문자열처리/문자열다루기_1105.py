# isdecimal(), isdigit(), isnumeric()
# => 주어진 문자열이 숫자로 되어있는지 검사하는 함수
# 음수에 적용하려면 "-12345".lstrip("-").isdigit()
# cf) isalpha() : 모두 알파벳
#     isalnum() : 영문 + 숫자


def solution(s):
    answer = True
    if len(s) == 4 or len(s) == 6:
           
        if s.isnumeric():
            return True
        else:
            return False
    else:
        return False