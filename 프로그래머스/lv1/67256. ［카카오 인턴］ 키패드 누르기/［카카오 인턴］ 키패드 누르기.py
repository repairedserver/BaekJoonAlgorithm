def solution(numbers, hand):
    ans = ''
    pad = {'1':(0,0), '2':(0,1), '3':(0,2),
           '4':(1,0), '5':(1,1), '6':(1,2),
           '7':(2,0), '8':(2,1), '9':(2,2),
           '*':(3,0), '0':(3,1), '#':(3,2)
        }
    l = pad['*']
    r = pad['#']
    
    for n in numbers:
        if n == 1 or n == 4 or n == 7:
            ans += 'L'
            l = pad[str(n)]
        
        elif n == 3 or n == 6 or n == 9:
            ans += 'R'
            r = pad[str(n)]
        
        else:
            ld = abs(l[0]-pad[str(n)][0]) + abs(l[1]-pad[str(n)][1])
            rd = abs(r[0]-pad[str(n)][0]) + abs(r[1]-pad[str(n)][1])
            
            if ld < rd:
                ans += 'L'
                l = pad[str(n)]
            
            elif ld > rd:
                ans += 'R'
                r = pad[str(n)]
            
            else:
                if hand == 'right':
                    ans += 'R'
                    r = pad[str(n)]
                else :
                    ans += 'L'
                    l = pad[str(n)]
    
    return ans