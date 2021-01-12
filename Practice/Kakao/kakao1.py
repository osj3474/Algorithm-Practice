# 2, 7, 17, 18, 20, 21, 23, 27   # 통과못하는 테스트케이스
import math

# 함수 : splitWord
# 역할 : 단어를 unit 단위로 쪼개어 리스트로 반환하는 함수
def splitWord(word, length, unit):
    ret = [0] * math.ceil(length/unit)   # 나눠질 갯수 길이 만큼의 리스트 생성
    i = 0
    for start in range(0, length, unit): # word 길이 만큼 반복문 (공차:unit)
        end = start + unit          # 마지막 인덱스
        if end >= length:           # word 길이를 초과하지 않는지 확인
            ret[i] = word[start:]   # 초과한다면, start로만 슬라이싱
        else:
            ret[i] = word[start:end]
        i += 1
    return ret     # 쪼개진 단어들을 담고 있는 리스트

# 함수 : makeNew
# 역할 : 새로운 단어의 길이를 반환하는 함수
def makeNew(word_lst, length, unit):
    cnt = length   # 원래 전체 길이
    flag = 1       # flag는 word 앞에 숫자를 넣어야 하는지
    for i in range(len(word_lst)-1):      # 나눠진 word를 하나씩 접근
        if word_lst[i] == word_lst[i+1]:  # 앞, 뒤 word가 같으면
            cnt -= unit   # unit 만큼 빼고
            if flag:
                cnt += 1  # 같은 걸 처음 만난 거라면, word앞에 숫자가 더해짐
            flag = 0
        else:
            flag = 1
    return cnt

def solution(s):
    length = len(s)
    if length == 1:    # 길이가 1인 경우는 따로 처리
        return 1

    limit = len(s)//2  # 쪼갤 단위의 최대치 # // : 몫
    MIN = 100000
    for unit in range(1, limit+1):
        word_lst = splitWord(s, length, unit) # word_lst = [ab, ca, bc, ..]
        cnt = makeNew(word_lst, length, unit) # result반환
        MIN = min(MIN, cnt)
    return MIN

def main():
    s = "abcabcabcabcdededededede"
    print(solution(s))

if __name__ == '__main__':
    main()