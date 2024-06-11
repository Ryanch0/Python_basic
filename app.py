file = open('a.txt','w') #wirte mode #기존 파일이 있어도 덮어쓰기 개념
file.write('hi')
file.close()

file = open('a.txt', 'a') #append mode 자료추가
file.write('\nzzzz')  #\n 줄바꿈
file.close()

file = open('a.txt', 'r') #read mode
print(file.read())
file.close()

f = open('data.csv', 'w') #excel file 
f.write('kim, lee, park')
f.write('\nkim, lee, park')
f.close()

list = ['samsung', 'kakao', 'naver', 'sinpoong']

ff = open('list.txt', 'w')
for i in list:
    ff.write(i+ '\n')
ff.close()

def 구구단(n):
    for i in range(1,10):
        print(f'{n}x{i} = {n*i}')

구구단(9)