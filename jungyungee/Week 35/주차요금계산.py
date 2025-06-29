def time_to_minutes(t):
    h, m = map(int, t.split(":"))
    return h * 60 + m

def solution(fees, records):
    base_time, base_fee, unit_time, unit_fee = fees
    in_times = {}     # 차량번호 : 마지막 입차 시간
    acc_times = {}    # 차량번호 : 누적 주차 시간

    for i in records:
        time_str, car, action = i.split()
        time = time_to_minutes(time_str)

        if action == "IN":
            in_times[car] = time
        else:  # OUT
            in_time = in_times.pop(car)
            duration = time - in_time
            acc_times[car] = acc_times.get(car, 0) + duration

    # 출차 안 된 차량 처리
    for car, in_time in in_times.items():
        duration = time_to_minutes("23:59") - in_time
        acc_times[car] = acc_times.get(car, 0) + duration

    # 요금 계산
    def calculate_fee(time):
        if time <= base_time:
            return base_fee
        extra = (time - base_time + unit_time - 1) // unit_time
        return base_fee + extra * unit_fee

    # 차량 번호 오름차순으로 요금 계산 결과 반환
    answer = []
    for car in sorted(acc_times):
        answer.append(calculate_fee(acc_times[car]))

    return answer