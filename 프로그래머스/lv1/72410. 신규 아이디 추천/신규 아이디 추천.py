def solution(new_id):
    ans = ''
    new_id = new_id.lower()
    for i in new_id:
        if i.islower() or i.isdigit() or i in ['-', '_', '.']:
            ans += i
    while '..' in ans:
        ans = ans.replace('..', '.')
    if ans[0] == '.':
        if len(ans) >= 2:
            ans = ans[1:]
        else:
            ans = '.'
    if ans[-1] == '.':
        ans = ans[:-1]
    if ans == '':
        ans = 'a'
    if len(ans) >= 16:
        ans = ans[:15]
        if ans[-1] == '.':
            ans = ans[:-1]
    while len(ans) < 3:
        ans += ans[-1]
    return ans