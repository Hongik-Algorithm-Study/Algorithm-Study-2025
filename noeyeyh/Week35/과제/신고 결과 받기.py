def solution(id_list, report, k):
    # 중복 제거
    report = set(report)
    
    # 각 사용자가 신고당한 횟수를 저장할 딕셔너리 초기화
    reported_count = {user: 0 for user in id_list}
    # 각 사용자가 신고한 사람들 목록을 저장할 딕셔너리 초기화
    reporter_dict = {user: [] for user in id_list}
    
    for r in report:
        # 각 신고 문자열을 신고자와 피신고자로 분리
        reporter, reported = r.split()
        reporter_dict[reporter].append(reported)
        reported_count[reported] += 1

    # 정지된 사용자 리스트
    suspended_users = set(user for user, cnt in reported_count.items() if cnt >= k)

    # 메일 받은 횟수 계산
    answer = []
    for user in id_list:
        count = 0
        for reported in reporter_dict[user]:
            if reported in suspended_users:
                count += 1
        answer.append(count)

    return answer
