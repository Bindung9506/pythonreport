print("20202727_김상현")

def input_type(input_str):
    if input_str.isalpha():
        return '글자입니다.'
    elif input_str.isdigit():
        return '숫자입니다.'
    elif input_str.isalnum():
        return '글자+숫자입니다.'
    else:
        return '모르겠습니다.'

user_input = input("문자열 입력: ")
result = input_type(user_input)
print(result)
