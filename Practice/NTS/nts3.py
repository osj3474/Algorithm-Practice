def solution(histogram):
    length = len(histogram)
    MAX = 0
    for i in range(length-2):
        for j in range(i+2, length):
            area = min(histogram[i],histogram[j])*(j-i-1) # H*W
            if MAX < area:
                MAX = area
    return MAX

def main():
    histogram = [6, 5, 7, 3, 4, 2]
    print(solution(histogram))

main()