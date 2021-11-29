#처음 짯던 코드인데, 프로그래머스에서는 돌아가나 스스로 새로운 리스트를 만들어보았을 때 오류가 발생한다. 
#인덱싱 순서가 맞아떨어졌던 우연인 것 같다. 

def solution(participant, completion):
    answer=0
    s_part=sorted(participant)
    s_comple=sorted(completion)
    s_comple.append(s_comple[-1])
    
    for i in range(len(s_part)): 
        if s_part[i]!=s_comple[i]:
            answer=s_part[i]
    
    return answer


#오류없이 다시 짠 코드 

def solution(participant, completion):
    answer=[]
    s_part=sorted(participant)
    s_comple=sorted(completion)

    for i in range(len(s_comple)):
        if (s_part[i]!=s_comple[i]):
            answer.append(s_part[i])
    if answer==[] :
        answer.append(s_part[-1])
    
    return answer[0]

