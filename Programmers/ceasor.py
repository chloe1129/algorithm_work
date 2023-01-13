def solution(s, n):
    answer = ''

    if len(s) >= 1:
        for i in s:
            if i == " ":
                answer += " "
            else:
                if 65<=ord(i)<=90 and ord(i)+n<=90:
                    answer += chr(ord(i)+n)
                elif 65<=ord(i)<=90 and 90<ord(i)+n:
                    answer += chr(ord(i)+n-26)
                elif 97<=ord(i)<=122 and ord(i)+n<=122:
                    answer += chr(ord(i)+n)
                elif 97<=ord(i)<=122 and 122<ord(i)+n:
                    answer += chr(ord(i)+n-26)
                    
    return answer

print(solution("Z  z",1))