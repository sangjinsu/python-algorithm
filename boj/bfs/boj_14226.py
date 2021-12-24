S = int(input())

queue = [{'imo': 1, 'sec': 0}]
while queue:
    status = queue.pop(0)
    if status.get('imo') == S:
        print(status.get('sec'))
        break
    queue.append({'imo': status.get('imo') * 2, 'sec': status.get('sec') + 2})
    if status.get('imo') > 0:
        queue.append({'imo': status.get('imo') - 1, 'sec': status.get('sec') + 1})
