#내가 짠 코드

def solution(n):
    answer=''
    if n%2==0: 
      answer='수박'*(n//2)
    else: 
      answer='수'+'박수'*(n//2)
    return answer
  
#타인코드 1

def water_melon(n):
    s = "수박" * n
    return s[:n]
 
#타인코드 2

def water_melon(n):
    return ("수박"*n)[0:n]
 
#심정: 어떻게 이 간단한 코드를 난 저렇게 복잡하게 짯을까? 
