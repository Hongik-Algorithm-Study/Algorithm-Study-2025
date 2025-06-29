import math

def time_to_min(time):
    h, m = map(int, time.split(":"))
    return h * 60 + m

def solution(fees, records):
    base_time, base_fee, unit_time, unit_fee = fees
    parking = {}    # 차량 번호별 입차 시간 저장
    total_time = {} # 차량 번호별 누적 시간 저장

    for record in records:
        time, car, state = record.split()
        minute = time_to_min(time)

        if state == "IN":
            parking[car] = minute
        else:  # OUT
            in_time = parking.pop(car)
            total_time[car] = total_time.get(car, 0) + (minute - in_time)

    # 아직 출차 안 한 차들 23:59 출차 처리
    for car, in_time in parking.items():
        total_time[car] = total_time.get(car, 0) + (time_to_min("23:59") - in_time)

    # 차량 번호 정렬 후 요금 계산
    answer = []
    for car in sorted(total_time):
        t = total_time[car]
        if t <= base_time:
            fee = base_fee
        else:
            extra = math.ceil((t - base_time) / unit_time)
            fee = base_fee + extra * unit_fee
        answer.append(fee)

    return answer
