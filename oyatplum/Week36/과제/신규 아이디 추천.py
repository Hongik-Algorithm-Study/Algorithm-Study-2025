import re
def solution(new_id):
    new_id = new_id.lower() #1단계

    for i in new_id: #2단계
        if i.isalpha() or i.isdigit():
            continue
        else:
            if i != '-' and i != '_' and i != '.':
                new_id = new_id.replace(i, "")

    new_id = re.sub('\.+', '.', new_id) #3단계

    if new_id.startswith('.'): #4단계
        new_id = new_id[1:]
    if new_id.endswith('.'):
        new_id = new_id[:len(new_id)-1]

    if new_id == '': #5단계
        new_id = 'a'

    if len(new_id) >= 16: #6단계
        new_id = new_id[:15]
        if new_id.endswith('.'):
            new_id = new_id[:len(new_id)-1]

    if len(new_id) <= 2:
        last = new_id[len(new_id)-1]
        while len(new_id) < 3:
            new_id += last

    return new_id