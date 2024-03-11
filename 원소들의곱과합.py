def solution(num_list):
    total = 1
    for i in num_list:
        total *= i
    if total < (sum(num_list))**2:
        answer = 1
    else:
        answer = 0
    return answer