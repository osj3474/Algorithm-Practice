def solution(genres, plays):
    play_lst = list(zip(genres, plays))
    genre_dic = {}
    play_cnt_dic = {}
    answer = []

    for i in range(len(play_lst)):
        genre_name = play_lst[i][0]
        if genre_name not in genre_dic:
            genre_dic[genre_name] = list()
            play_cnt_dic[genre_name] = 0
        genre_dic[genre_name].append((i, play_lst[i][1]))
        play_cnt_dic[genre_name] += play_lst[i][1]

    play_cnt_lst = list()
    for key, item in play_cnt_dic.items():
        play_cnt_lst.append([key, item])

    play_cnt_lst = sorted(play_cnt_lst, key=lambda x: -x[1])
    for play in play_cnt_lst:
        genre = play[0]
        genre_dic[genre] = sorted(genre_dic[genre], key=lambda x:(-x[1], x[0]))
        answer.append(genre_dic[genre][0][0])
        try:
            answer.append(genre_dic[genre][1][0])
        except:
            pass

    return answer


def main():
    genres = ["classic", "pop", "classic", "classic", "pop"]
    plays = [500, 600, 150, 800, 2500]
    print(solution(genres, plays))

main()
