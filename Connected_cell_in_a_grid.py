def maxRegion(grid): 
    n = len(grid) 
    m = len(grid[0]) 
    answer = [] 
    visited = [[0 for _ in range(m)] for _ in range(n)] 
    # ��ǥ ���� ����Ʈ. ���� �밢�� ������ �ð���� ��ȸ. 
    dx = [-1, -1, -1, 0, 1, 1, 1, 0 ] 
    dy = [-1, 0, 1, 1, 1, 0, -1, 1 ] 
    for i in range(n): 
        for j in range(m): 
            # grid ���� 1�̰�, ���� �湮���� ���� �� 
            if grid[i][j] == 1 and visited[i][j] == 0: 
                stack = [(i, j)] 
                visited[i][j] = 1 
                cnt = 1 
                while stack: 
                    x, y = stack.pop() 
                    for dir in range(8): 
                        next_x = x + dx[dir] 
                        next_y = y + dy[dir] 
                        
                        if (0 <= next_x < n and 0 <= next_y < m) and (grid[next_x][next_y] and visited[next_x][next_y]) == 0: 
                            stack.append((next_x, next_y)) 
                            # stack�� �߰��� �� visited�� 1�� �ٲ��༭ ���߿� �湮�� ���� stack�� �ߺ��ؼ� ���� �ʵ��� ��. 
                            visited[next_x][next_y] = 1 
                            cnt += 1 
                answer.append(cnt) 
    return max(answer)