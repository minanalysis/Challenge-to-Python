# +
n = int(input('숫자를 적어주세요' ))
t = str(input('이름을 적어주세요' ))

a=list(range(1,n))
b=sorted(list(range(1,n)),reverse=True)

print("{}가 그려본".format(t))

for i in a:
    print(i*'*')
for ii in b : 
    if ii != n-1 :
        print(ii*'*')


# -
## format함수를 통해, 이름 input값을 print해줄 수 있다. --> 유용한듯!
## 별그리기 경우, 절댓값 함수를 통해서 그려주는 방법이 따로 있는데, 한번 더 이해가 필요해서 따로 커밋할 예정. 
