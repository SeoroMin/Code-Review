def minion_game(string):
    # your code goes here
    vowels = 'AEIOU'
    s_score = 0
    k_score = 0
    
    for i in range(len(string)):
        # �κ� ���ڿ��� ����
        temp_score = len(string) - i
        
        # ���ڿ� �� �ش� ���ڰ� ������ ��
        if string[i] in vowels:
            k_score += temp_score
        # ������ ��
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