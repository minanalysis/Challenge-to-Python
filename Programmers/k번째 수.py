def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        a=commands[i][0]
        b=commands[i][1]
        c=commands[i][2]
        answer.append(sorted(array[a-1:b])[c-1])
    return answer

#처음으로 온전히 호다닥 풀고 신이 났다. 
