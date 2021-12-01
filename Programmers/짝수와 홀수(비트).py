#이문제는 엄청 쉬웠다. 
#그래도 한개씩 손이 기억하도록 계속 연습해야지 

# 정수 num이 짝수일 경우 "Even"을 반환하고 홀수인 경우 "Odd"를 반환하는 함수

# 내 풀이 
def solution(num):
    if num%2 == 0 : answer="Even"
    elif num%2 == 1 : answer="Odd"
    return answer
  
# 다른사람 풀이 

def evenOrOdd(num):
    return ["Even", "Odd"][num & 1]
 
#엄청 신선하게 다가온 풀이 -> 비트연산자 이용 
#비트연산자인 &(AND 연산자)를 사용한다

#2진법으로 숫자를 바꾸면 1의 자리 숫자는 0 아니면 1이다
#1의 자리가 1이면 홀수, 0이면 짝수라고 볼 수 있다

#예를들어, 3은 2진수로 11 
#[11&1]->1 
#1을 인덱싱하면 'Odd'
