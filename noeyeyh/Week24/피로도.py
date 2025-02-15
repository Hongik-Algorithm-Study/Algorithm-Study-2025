import itertools

def solution(k, dungeons):
    answer = 0
    permutations = list(itertools.permutations(dungeons, len(dungeons)))

    for i in range(len(permutations)):
        count = 0
        remaining_energy = k
        
        for min_energy_required, energy_consumed in permutations[i]:
            if remaining_energy >= min_energy_required:
                remaining_energy -= energy_consumed
                count += 1
                
        if count > answer:
            answer = count
            
    return answer 