
string = 'abcd'

string.replace('b', 'B')

print(string) # 문자열은 변경할 수 없으므로 abcd 가 그대로 출력된다. 

print(string.replace('b', 'B')) # replace 메서드를 사용하면 원본은 그대로이고, 변경된 새로운 문자열 객체를 리턴한다.