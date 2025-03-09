def solution(routes):
    routes.sort(key=lambda x: x[1])  # 끝점 기준으로 정렬

    answer = 0
    last_camera_position = -30001

    for route in routes:
        start, end = route
        # 현재 차량의 시작점이 마지막 카메라 위치보다 뒤에 있을 경우 카메라 설치
        if start > last_camera_position:
            answer += 1 
            last_camera_position = end

    return answer