import datetime
def solution(a, b):
    answer = 'MON TUE WED THU FRI SAT SUN'.split()
    return answer[datetime.datetime(2016, a, b).weekday()]