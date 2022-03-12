def maxRegion(grid): 
    n = len(grid) 
    m = len(grid[0]) 
    answer = [] 
    visited = [[0 for _ in range(m)] for _ in range(n)] 
    # 좌표 방향 리스트. 왼쪽 대각선 위부터 시계방향 순회. 
    dx = [-1, -1, -1, 0, 1, 1, 1, 0 ] 
    dy = [-1, 0, 1, 1, 1, 0, -1, 1 ] 
    for i in range(n): 
        for j in range(m): 
            # grid 값이 1이고, 아직 방문하지 않을 때 
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
                            # stack에 추가할 때 visited를 1로 바꿔줘서 나중에 방문할 곳을 stack에 중복해서 넣지 않도록 함. 
                            visited[next_x][next_y] = 1 
                            cnt += 1 
                answer.append(cnt) 
    return max(answer)