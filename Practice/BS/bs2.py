import heapq as hq

def gcd(a, b):
    while b>0:
        q = a//b
        r = a%b
        a = b
        b = r
    return a

def solution(n, times):
    GCD = gcd(times[0], times[1])
    for i in range(2, len(times)):
        GCD = gcd(GCD, times[i])
    LCD = 1
    for time in times:
        LCD *= time//GCD
    LCD*=GCD

    chunk = 0
    for time in times:
        chunk += LCD//time
    answer = 0
    answer = LCD * (n // chunk)

    n = n % chunk

    minutes = dict()
    for i in range(len(times)):
        minutes[i] = times[i]
        times[i] = [times[i], i]
    hq.heapify(times)

    while 1:
        item = hq.heappop(times)
        n -= 1
        if n == 0:
            break
        item[0] += minutes[item[1]]
        hq.heappush(times, item)
    return item[0]

def main():
    n = 6
    times = [7,10]
    print(solution(n, times))

main()



