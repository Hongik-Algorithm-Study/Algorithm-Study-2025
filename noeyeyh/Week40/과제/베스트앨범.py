def solution(genres, plays):
    genres_plays = {}
    genre_tracks = {}
    answer = []
    
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        
        if genre in genres_plays:
            genres_plays[genre] += play
        else:
            genres_plays[genre] = play
        
        if genre in genre_tracks:
            genre_tracks[genre].append((play, i))  # (재생 횟수, 인덱스) 튜플로 저장
        else:
            genre_tracks[genre] = [(play, i)]

    sorted_genres = sorted(genres_plays.items(), key=lambda x: x[1], reverse=True)

    for genre, _ in sorted_genres:
        sorted_tracks = sorted(genre_tracks[genre], key=lambda x: x[0], reverse=True)
        
        for play_count, index in sorted_tracks[:2]:
            answer.append(index)

    return answer
