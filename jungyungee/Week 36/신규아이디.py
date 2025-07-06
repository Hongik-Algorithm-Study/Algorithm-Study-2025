def solution(new_id):
    new_id = new_id.lower()
    
    allowed = ''
    for i in new_id:
        if i.isalnum() or i in ['-', '_', '.']:
            allowed += i
    new_id = allowed
    
    result = ''
    pre = ''
    for i in new_id:
        if i == '.' and pre == '.':
            continue
        result += i
        pre = i
    new_id = result
    
    if new_id.startswith('.'):
        new_id = new_id[1:]
    if new_id.endswith('.'):
        new_id = new_id[:-1]
    
    if new_id == '':
        new_id = 'a'
    
    new_id = new_id[:15]
    if new_id.endswith('.'):
        new_id = new_id[:-1]
    
    while len(new_id) < 3:
        new_id += new_id[-1]
    
    return new_id