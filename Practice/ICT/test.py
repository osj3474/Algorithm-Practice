'''
Name: 오상진
Student ID: 21500404
Description: 이 프로그램은 connected component labeling을 해주는 프로그램 입니다.
'''

# 필요한 library를 import합니다.
from PIL import Image
from os.path import splitext
from disjointset import DisjointSetManager
from random import randint

# Connected-Component Labeling을 위해서는 해당 이미지를 
# 1. 일단 binary image로 바꿔줘야 한다.
# 2. background가 아닌 영역에서 CC를 찾고 각 componet마다 다른 색깔을 부여한다.

# 글로벌 변수로 white와 black의 r,g,b 값을 설정해준다.
white = (255, 255, 255)
black = (0, 0, 0)


# 파일 경로를 넣으면, ccl해서 jpg 파일을 저장하는 함수
# input :파일 경로, threshold, reverse_color
# return : 없음
def label_ccs(file_path, threshold=50, reverse_color=False):
    img = Image.open(file_path)  # 해당경로에서 img파일을 연다.
    data = img.load()  # data에 해당 img를 넣는다.
    w, h = img.size  # w, h에 해당 img의 너비와 높이를 넣는다.

    convert_rgb_into_bw(data, w, h, threshold, reverse_color)  # binary image로 변환

    partition = find_ccs(data, w, h)  # partition에 dictionary의 values 값 // [(v1,v2), (v4)]
    assign_random_color(data, partition)  # sub_set별로 다른 random한 색깔을 할당한다.

    file, ext = splitext(file_path)  # 기존 파일의 파일명과 확장자명을 분리한다.
    img.save(file + '_ccl.jpg', 'JPEG')  # ccl 처리가 된 이미지를 저장한다.


# 해당 파일을 binary image로 바꿔주는 함수
# input : img.load()된 data
# return : 없음 
def convert_rgb_into_bw(data, w, h, threshold, reverse_color):
    c1, c2 = (white, black) if reverse_color else (black, white)  # reverse값을 True로 주면 색을 반대로
    for y in range(h):
        for x in range(w):
            r, g, b = data[x, y]
            if (r + g + b) / 3 < threshold:  # threshold보다 작으면 모두 white처리
                data[x, y] = c1
            else:
                data[x, y] = c2  # 아니면 black으로 채운다.


# 받은 data를 바탕으로 combine하고, vertex 묶음을 리턴해주는 함수
# input : img.load()된 data
# return : dictionary의 values 값 // [(v1,v2), (v4)]
def find_ccs(data, w, h):
    V = [(x, y) for y in range(h)  # vertex의 집합, V라는 dictionary 생성
         for x in range(w) if data[(x, y)] == white]
    dis_manager = DisjointSetManager(V)  # DisjointSet 생성 
    for v in V:
        for n in collect_neighbors(v, data, w, h):  # 해당 vertex와 연결된 vertex 집합
            dis_manager.combine(v, n)  # 그것들을 연결한다.
    return dis_manager.get_partition()  # dictionary value의 조합을 리턴.


# 해당 vertex와 연결된 vertex들을 리턴해주는 함수  
# input : vertex, data  ex) vertex = (1,2)
# return : vertex와 연결된 vertex들 ex) {(0,3), (1,1), (1,3), (2,2)}
def collect_neighbors(v, data, w, h):
    # 넘겨받은 vertex의 x, y 좌표
    (x, y) = v
    # return할 리스트
    c_list = []
    # row나 col이 0 or w or h 인 경우는 비교할 필요 없음.
    for i in range(3):
        for j in range(3):
            a = x + 1 - i  # 비교를 할 vertex의 x좌표이다.
            b = y + 1 - j  # 비교를 할 vertex의 y좌표이다.
            if (a == w or b == h or a < 0 or b < 0) or (a == x and b == y):
                continue  # 해당 좌표가 w, h, 0 의 boundary를 넘어가면 비교하지 않는다.
            if data[(a, b)] == white:
                c_list.append((a, b))  # white에 해당하는 vertex를 묶어준다.
    return c_list


# 각 partition마다 다른 color를 입힌다.
# input : data, partition
# return : 없음.
def assign_random_color(data, partition):
    for sub_set in partition:
        # sub_set별로 다른 색을 할당해야하기 때문에 여기서 randint를 사용한다.
        col = (randint(50, 255), randint(50, 255), randint(50, 255))
        for sub_element in sub_set:
            data[sub_element] = col  # 해당 color값을 할당한다.


label_ccs("images/flowers.jpg")
label_ccs("images/fruits.jpg", 240, True)
label_ccs("images/solar.jpg", 50)

