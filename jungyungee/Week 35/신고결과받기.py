def solution(id_list, report, k):
    report = list(set(report))
    reported_count = {}
    report_map = {}
    suspended_list = []
    answer = [0 for _ in range(len(id_list))]
    
    # 신고당한 유저 찾기
    for i in report:
        reporter, reported = i.split()
        if reporter not in report_map:
            report_map[reporter] = set()
        if reported not in report_map[reporter]:
            report_map[reporter].add(reported)
            reported_count[reported] = reported_count.get(reported, 0) + 1
            
    # 정지당한 유저 찾기 
    for i in id_list:
        if reported_count.get(i, 0) >= k:
            suspended_list.append(i)
            
    # 각 유저별로 처리결과 받을 수 구하기 
    for i in range(len(id_list)):
        if id_list[i] in report_map:
            for j in report_map[id_list[i]]:
                if j in suspended_list:
                    answer[i] += 1
                
    return answer