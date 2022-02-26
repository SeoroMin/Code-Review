def minion_game(string):
    # your code goes here
    vowels = 'AEIOU'
    s_score = 0
    k_score = 0
    
    for i in range(len(string)):
        # 부분 문자열의 개수
        temp_score = len(string) - i
        
        # 문자열 중 해당 문자가 모음일 시
        if string[i] in vowels:
            k_score += temp_score
        # 자음일 시
        else:
            s_score += temp_score
        
    if s_score == k_score:
        print('Draw')
    elif s_score > k_score:
        print('Stuart', s_score)
    else:
        print('Kevin', k_score)

if __name__ == '__main__':
    s = input()
    minion_game(s)